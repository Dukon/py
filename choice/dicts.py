#!/usr/bin/env python
# -*- coding: utf-8 -*-

C = { u"a" : 10,
      u"b" : 1234,
      u"c" : 9877
    }

L = C.keys()
L.sort()    
for (K, V) in C.iteritems() :
    print K, V