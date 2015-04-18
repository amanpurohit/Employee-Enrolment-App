# -*- coding: utf-8 -*-
"""
    __init__.py

    :copyright: (c) 2015 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
from trytond.pool import Pool
from test import PersonalDetails, Education


def register():
    Pool.register(
        PersonalDetails,
        Education,
        module='test', type_='model'
    )
