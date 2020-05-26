#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2

import sys 


def _usage():
    print("""
Usage: {script} ALGO IMG_PATH

Available algorithms:
- {algos}
""".format(script=sys.argv[0], algos='\n- '.join(get_algo_handlers())), file=sys.stderr)
    sys.exit(128)


def get_algo_handlers():
    return {
        'sobel': sobel_algo,
        'canny': canny_algo
    }


def sobel_algo(image):
    blured_img = cv2.GaussianBlur(image, (3, 3), 0)
    gray = cv2.cvtColor(blured_img, cv2.COLOR_BGR2GRAY)

    def sobel_wrapper(dx, dy):
        return cv2.Sobel(
                        gray, 
                        cv2.CV_16S, 
                        dx, 
                        dy, 
                        ksize=3, 
                        scale=1, 
                        delta=0,
                        borderType=cv2.BORDER_DEFAULT)
    
    grad_x = sobel_wrapper(1, 0)
    grad_y = sobel_wrapper(0, 1)

    abs_grad_x = cv2.convertScaleAbs(grad_x)
    abs_grad_y = cv2.convertScaleAbs(grad_y)

    return cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)


def canny_algo(image):
    return cv2.Canny(image, 100, 200)


def main(args):
    try:
        algo, path = args
    except ValueError:
        _usage()        

    if algo not in get_algo_handlers().keys():
        print('ERROR: Unknow algorithm: {}'.format(algo), file=sys.stderr)
        _usage()

    src_img = cv2.imread(path, cv2.IMREAD_COLOR)
    if src_img is None:
        print('ERROR: No such file: {}'.format(path), file=sys.stderr)
        _usage()
    
    result = get_algo_handlers()[algo](src_img)
    cv2.imshow('result from {}'.format(algo), result)
    cv2.waitKey(0)


if __name__ == '__main__':
    main(sys.argv[1:])