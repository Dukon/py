#!/usr/bin/env python
# -*- coding: utf-8 -*-

# A = [ 1, 3.0, 4, u"Vasya", u"Pupkin" ]
# for X in A :
    # print X, type(X)

# B = range (20,0,-1)
# for K in B :
    # print K
	
	# print B
def issimple (X) :
    for K in range( 2, X/2 ) :
        if X % K == 0 :
            return False
    return True
    
def simple( N ) :
    K = 2
    while K<N :
        if issimple(K):
            yield K
        K+=1
    
    
for X in simple(50) :
    print X