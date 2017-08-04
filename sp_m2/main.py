#!/usr/bin/env python
# -*- coding: utf-8 -*-

import doc

N = doc.Nakladnaya()

N.append ('Рога', 25, unit='шт', price=100.02)
N.append(doc.Position ('Копыта', 100, summa=1000.45))

print (N)