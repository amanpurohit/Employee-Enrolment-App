# -*- coding: utf-8 -*-
"""
    test.py

    :copyright: (c) 2015 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
from trytond.model import fields, ModelSQL, ModelView
from trytond.pool import PoolMeta
from trytond.pyson import Eval
from datetime import date, timedelta

__all__ = ['PersonalDetails', 'Education']

__metaclass__ = PoolMeta

STATES = {
    'readonly': ~Eval('active', True)
}

DEPENDS = ['active']


class PersonalDetails:

    "Personal Details"
    __name__ = "party.party"

    gender = fields.Selection([
        ('male', 'M'),
        ('female', 'F'),
        ('undefined', 'Do not wish to mention'),
    ], 'Gender', required=True,
        states=STATES, depends=DEPENDS)

    date_of_birth = fields.Date(
        "Date of Birth", required=True, states=STATES, depends=DEPENDS
    )

    place_of_birth = fields.Char(
        "Place of Birth", required=True, states=STATES, depends=DEPENDS
    )

    height = fields.Numeric(
        "Height", states=STATES, depends=DEPENDS
    )

    weight = fields.Numeric(
        "Weight", states=STATES, depends=DEPENDS
    )

    blood_group = fields.Char(
        "Blood Group", states=STATES, depends=DEPENDS
    )

    identification_mark = fields.Char(
        "Identification Mark", states=STATES, depends=DEPENDS
    )

    pan_card_number = fields.Char(
        "PAN Card Number",
        size=10,
        required=True,
        states=STATES,
        depends=DEPENDS)

    marital_status = fields.Selection([
        ('single', 'Single'),
        ('married', 'Married')
    ], 'Maritial Status', required=True, states=STATES, depends=DEPENDS
    )

    hobbies = fields.Text(
        "Hobbies", states=STATES, depends=DEPENDS
    )

    education = fields.One2Many(
        'party.education',
        'party', 'Education', states=STATES, depends=DEPENDS
    )

    @staticmethod
    def default_gender():
        return 'male'

    def pre_validate(self):
        user_dob = self.date_of_birth
        current_date = date.today()
        if ((current_date - user_dob) < timedelta(hours=7300)):
            raise ValueError("Date of birth not valid")


class Education(ModelSQL, ModelView):

    'Education'
    __name__ = 'party.education'

    party = fields.Many2One(
        'party.party', 'Party', required=True,
        select=True
    )
    degree = fields.Char(
        "Degree",
        required=True,
        states=STATES)
    stream = fields.Char(
        "Stream",
        required=True,
        states=STATES)
    grade = fields.Char("Grade", required=True, states=STATES)
    university = fields.Char(
        "University",
        required=True,
        states=STATES)
    year_of_completion = fields.Char(
        "Year of Completion",
        required=True,
        states=STATES)
