#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def sqeq ( a=1.0, b=1.0, c=0.1 ) :
    try :
        D = b*b - 4*a*c
        if D < 0 :
            return []
        else :
            x1 = ( -b + math.sqrt( D ) )/(2 * a)
            x2 = ( -b - math.sqrt( D ) )/(2 * a)
            return [ x1, x2 ]
    except ZeroDivisionError :
        x = -c / b
        return [ x, None ]

if __name__ == "__main__" :
    print sqeq( 1, -5, 6 )
    print sqeq( 2, -10, 12 )
    print sqeq( 0, 2, 3 )
    print sqeq( 1, -5, 200 )