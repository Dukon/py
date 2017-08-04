#!/usr/bin/python3
# -*- coding: utf-8 -*-

from contextlib import suppress
from datetime import datetime
import logging

import sp_m2.helpers as hlp
from .Position import *

class Nakladnaya ( object ) :

    def __init__(self) :
        self.__Created = datetime.now()
        self.__Positions = []

    created = property (lambda self : self.__Created)

    @property
    def number(self):
        return self.__Number

    @number.setter
    @hlp.info_value
    @hlp.value_not_none
    def number(self, value):
       # logging.info ('Number changed from {0} to {1}'.format(self.number, value))
        self.__Number = value

    @number.deleter
    def number(self):
        logging.info('Number {0} deleted'.format(self.number))
        del self.__Number

    #@property
    #def address(self):
    #    return self.__Address

    address = property(lambda self : self.__Address)

    @address.setter
    @hlp.trace_value(logging.WARNING)
    @hlp.value_not_none
    def address(self, value):
        logging.warning('Address changed')

        # responser

    responser = property(lambda self : self.__Responser)

    @responser.setter
    @hlp.trace_value(logging.ERROR - 1)
    @hlp.value_not_none
    def responser (self, value ):
        self.__Responser = value

    subscribed = property(lambda self : False)

    @property
    def itogo (self):
        if self.subscribed :
            return self.__Itogo
        else:
            return sum(p.summa for p in self.__Positions)

    def append(self, *args, **kwargs):
        if isinstance(args[0],Position):
            P = args[0]
        else:
            P = Position(*args, **kwargs)
        self.__Positions.append(P)

    __StrData = [
        ('Number', 'number'),
        ('Creation date', 'created'),
        ('Address', 'address'),
        ('Responsible person', 'responser'),
        ('Is subscribed', 'subscribed'),
        ('Result', 'itogo'),

    ]

    def __str__(self):
        L = []
        for text, propname in type(self).__StrData:
            with suppress (AttributeError) :
                T = '{0}: {1}'.format(text, getattr(self, propname))
                L.append(T)
        L += map( str, self.__Positions )

