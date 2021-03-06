#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

def value_not_none(method):
    def checked_method(self, value):
        if value is None:
            raise ValueError('\'None\' is not alowed for property value')
        return method(self, value)
    checked_method.__name__ = method.__name__
    return checked_method

def trace_value(loglevel = logging.DEBUG):
    def tracing_method(method):
        def traced_method(self, value):
            pname = method.__name__
            old = getattr(self, pname)
            msg = ('Property \'{pname}\' will be changed '+
                  'from \'{old}\' to \'{value}\'').format(**locals())
            logging.log(loglevel, msg )
            return method(self, value)
        traced_method.__name__ = method.__name__
        return traced_method
    return tracing_method

debug_value = trace_value( logging.DEBUG   )
info_value  = trace_value( logging.INFO    )
warn_value  = trace_value( logging.WARNING )

