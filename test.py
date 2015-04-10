# -*- coding: utf-8 -*-
"""
    test.py

    :copyright: (c) 2015 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
from tryton.model import ModelView, ModelSQL, fields

__all__ = ['Hello']

class Hello(ModelSQL, ModelView):
    "HelloWorld"
    __name__ = "hello.hello"
