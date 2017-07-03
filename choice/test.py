#!/usr/bin/env python
# -*- coding: utf-8 -*-

def select_max (List, less) :
    if len(Liat) <= 0 : return None
    if len(List) == 1 : return List[0]
    Result = Liat[0]
    for K in Liat[1:] :
        if less(Result, K) :
            Result = K
    return Result

A = [ 1, 23, u"Vasya", 34, 12, 455 ]
B = [ 34, u"Petya" ]

if 1 not in A :
    print u"OK"
else :
    print u"No" 
    
print A + B
print 5*B
print A[2]
print A[1:3]
print A[:3]
print A[1:]
print A[-2:]
print len(A)
print min(A)
print max(A)

del A[1:3]
print A
print A.pop()
print A
print A.index(34)
A.remove(34)
print A
print (5*A).count(1)

A = [9,11, 219, 0]
A.sort ()
A.reverse()
print A

# def func ( selector ) :
    # if selector < 0 :
        # return lambda x : x*x
    # else : 
        # return lambda x : x*x*x

# def oper ( L, function ) :
    # Result = [ function(K) for K in L ]
    # return Result
        
# X = [ 1, 34, 67, 100 ]
# print oper ( X, func(1) )
# A = func
# func = u"This is not function"

# print func
# print A (3)
# X = None
# if A<0 :
    # fgfgfgfgfgfg
# else A == 1 : 
    # X = 0
	# gfgfgfgfgfg
	# fgfgfgfgfgfg
# else :
    # fgfgfgfgfgfg
	# fgfgfgfgfgfg
	# fgfgfgfgfgfg
	
# print X