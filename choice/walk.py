#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, os.path
import codecs
import csv
import hashlib

HS = hashlib.md5()
with codecs.open (u"file.txt", u"rb") as TRG :
    try :
        while True :
            A = TRG.read ( 1024 )
            if A == '' : break
            HS.update(A)
    except IOError : pass

print HS.hexdigest()
    
    
    # FMT = csv.writer(TRG)
    # FMT.writenow([u"Vasya", u"Pupkin", 120])
    # FMT.writenow([u"Chapaev", u"VI", 120])

# TRG.write(u"fhfjghfjgkhfdgkjfdhg")
    # for Line in SRC :
        # print Line,

# CDC = codecs.lookup(u"windows-1251")

# Cdrive = u"D:\\Work_py"
# for (path, dirs, files) in os.walk(Cdrive) :
    # for File in files :
        # P = os.path.join( path, File )
        # RP = os.path.relpath( P, Cdrive)
        # ( Str, N ) = CDC.encode( RP )
        # print Str
    # # if u"Application Data" in dirs :
        # # dirs.remove(u"Application Data")
    # # if u"Program Files" in dirs :
        # # dirs.remove(u"Program Files")
    # # print path