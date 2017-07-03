#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open (u"D:\\Work_py\\choice\\loop.py", "rt") as FD :
for Line in FD :
    L = Line[:-1] if Line[-1] == u'\n' else Line
    print L
# FD.close()
# TRG = open (u"D:\\Work_py\\choice\\test.txt", "wt")
# TRG.write(u"dddds")