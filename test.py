# -*- coding: utf-8 -*-
"""
    test.py

    :copyright: (c) 2015 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
from trytond.model import fields, ModelSQL, ModelView
from trytond.pool import PoolMeta

__all__ = ['Employee']
__metaclass__ = PoolMeta

STATES = {}

DEPENDS = []


class Employee(ModelSQL, ModelView):

    "Employee"
    __name__ = "company.employee"

    gender = fields.Selection([
        ('male', 'M'),
        ('female', 'F'),
        ('undefined', 'N/A'),
    ], 'Gender', required=True,
        states=STATES, depends=DEPENDS)

    passport_id = fields.Char(
        "Passport Id",
        size=15,
        states=STATES,
        depends=DEPENDS,
        required=True)

    pan = fields.Char(
        "PAN",
        size=10,
        states=STATES,
        depends=DEPENDS,
        required=True)

    _sql_error_messages = {
        'uniq_error': 'This field must be unique.',
        'null_error': 'This field must not be null'
    }

    @classmethod
    def __setup__(cls):
        super(Employee, cls).__setup__()
        cls._set_states_depends(['company', 'party'])

    @staticmethod
    def default_gender():
        return 'male'

    @classmethod
    def _set_states_depends(cls, arg_list):
        for string in arg_list:
            module = getattr(cls, string)
            module.states = STATES
            module.depends = DEPENDS
