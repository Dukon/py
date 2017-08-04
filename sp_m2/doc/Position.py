#!/usr/bin/env python
# -*- coding: utf-8 -*-

from contextlib import suppress

class Position (object):
    def __init__(self, title, quantity, **kwargs ):
        self.__Title = title
        self.__Quantity = quantity
        with suppress(KeyError):
            self.__Unit = kwargs['unit']
        with suppress(KeyError):
            self.__Price = kwargs['price']
        try:
            self.__Summa = kwargs['summa']
        except KeyError:
            try:
                self.__Summa = self.quantity * self.price
            except AttributeError as Exc:
                raise ValueError('Price or summa have to be specified') from Exc

    title    = property(lambda self : self.__Title   )
    quantity = property(lambda self : self.__Quantity)
    unit     = property(lambda self : self.__Unit    )
    price    = property(lambda self : self.__Price   )
    summa    = property(lambda self : self.__Summa   )