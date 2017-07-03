#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import subprocess
# import StringIO

#path = os.path.expandvars (u"%SystemRoot%\\system32\\notepad.exe")
#print path
path = u"C:\\Python27\\python.exe"

# SRC = StringIO.StringIO(u"Hello")

dir = subprocess.Popen ([path, u"mod.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE,)

X = u""
while dir.poll() == None :
    # sleep( 100 )
    ( cout, cerr ) = dir.communicate("Hello")
    X+=cout

# P = dir.communicate(u"This is a test")
# print P
dir.wait()

print dir.poll()
