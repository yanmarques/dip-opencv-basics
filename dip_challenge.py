#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtGui, QtCore

import sys
import cv2
import numpy as np
import main_gui


class DipChallengeApp(QtWidgets.QMainWindow, main_gui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(DipChallengeApp, self).__init__(parent)
        self.setupUi(self)

        # object containing the capture device
        self.cap = None

        # object containing the capture timer
        self.timer = None

        # wheter capture has started
        self.capture_started = False

        # when user clicks, start capturing
        self.takeCameraShot.clicked.connect(self._on_capture_timer)

    def _deduce_cvt_code(self):
        # commented because it can not work
        # Segmentation fault error
        #if self.appliesGrayScale.isChecked(): 
            # should apply gray scale
            #return cv2.COLOR_BGR2GRAY
        
        # video cames as BGR so covert to RGB
        return cv2.COLOR_BGR2RGB

    def _on_camera_shot(self):    
        # read a frame
        _, frame = self.cap.read()

        
        cvt_frame = cv2.cvtColor(frame, self._deduce_cvt_code())

        self._build_histogram(cvt_frame)

        self._create_image(self.cameraView, cvt_frame)

    def _build_histogram(self, frame):
        # split frame into correspondent planes
        bgr_planes = cv2.split(frame)
        hist_size, hist_range = 256, (0, 256)

        b_hist = cv2.calcHist(bgr_planes, [0], None, [hist_size], hist_range)
        g_hist = cv2.calcHist(bgr_planes, [1], None, [hist_size], hist_range)
        r_hist = cv2.calcHist(bgr_planes, [2], None, [hist_size], hist_range)

        hist_w = 400
        hist_h = 300
        bin_w = int(round(hist_w/hist_size))
        hist_image = np.zeros((hist_h, hist_w, 3), dtype=np.uint8)

        cv2.normalize(b_hist, b_hist, alpha=0, beta=hist_h, norm_type=cv2.NORM_MINMAX)
        cv2.normalize(g_hist, g_hist, alpha=0, beta=hist_h, norm_type=cv2.NORM_MINMAX)
        cv2.normalize(r_hist, r_hist, alpha=0, beta=hist_h, norm_type=cv2.NORM_MINMAX)

        for i in range(1, hist_size):
            cv2.line(hist_image, ( bin_w*(i-1), hist_h - int(b_hist[i-1].round()) ),
                    ( bin_w*(i), hist_h - int(b_hist[i].round()) ),
                    ( 255, 0, 0), thickness=2)
            cv2.line(hist_image, ( bin_w*(i-1), hist_h - int(g_hist[i-1].round()) ),
                    ( bin_w*(i), hist_h - int(g_hist[i].round()) ),
                    ( 0, 255, 0), thickness=2)
            cv2.line(hist_image, ( bin_w*(i-1), hist_h - int(r_hist[i-1].round()) ),
                    ( bin_w*(i), hist_h - int(r_hist[i].round()) ),
                    ( 0, 0, 255), thickness=2)
        
        self._create_image(self.histogramView, hist_image)

    def _create_image(self, view, frame):
        # create img widget from frame
        img = QtGui.QImage(frame, 
                           frame.shape[1], 
                           frame.shape[0], 
                           QtGui.QImage.Format_RGB888)

        # wrap image into ImageView
        pix = QtGui.QPixmap.fromImage(img)
        item = QtWidgets.QGraphicsPixmapItem(pix)
        
        scene = QtWidgets.QGraphicsScene(self)
        scene.addItem(item)
        view.setScene(scene)

    def _on_capture_timer(self, event):
        if self.capture_started:
            self._maybe_stop_capture_objects()
            self.takeCameraShot.setText('Start Capturing')
            self.capture_started = False
            return

        # get webcam device, index 0
        self.cap = cv2.VideoCapture(0)
        
        # try to read the first frame to check wheter it works
        _ret, frame = self.cap.read()
        if frame is None:
            print('ERRO: No webcam found/available.', file=sys.stderr)
            return

        # we take manually the first shot
        # just because when the timer timeout is high
        # we do not let the user waiting 
        self._on_camera_shot()

        # get timer counter
        self.timer = QtCore.QTimer()
        
        # keep taking camera shots
        self.timer.timeout.connect(self._on_camera_shot)
        
        # timesout every 66 miliseconds, seems like a video
        self.timer.start(1000/66)

        self.capture_started = True
        self.takeCameraShot.setText('Stop capturing')

    def _maybe_stop_capture_objects(self):
        # release capture device
        if self.cap:
            self.cap.release()

        # stop timer
        if self.timer:
            self.timer.stop()

    def deleteLater(self):
        self._maybe_stop_capture_objects()
        super(DipChallengeApp, self).deleteLater()


def main(args):
    app = QtWidgets.QApplication(args)
    window = DipChallengeApp()
    window.show()
    return app.exec_()    


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
