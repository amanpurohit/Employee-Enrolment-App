import sys
import os
import unittest
from contextlib import nested

import trytond.tests.test_tryton
from trytond.tests.test_tryton import POOL, DB_NAME, USER, CONTEXT
from trytond.exceptions import UserError
from trytond.transaction import Transaction
DIR = os.path.abspath(os.path.normpath(os.path.join(
    __file__, '..', '..', '..', '..', '..', 'trytond'
)))
if os.path.isdir(DIR):
    sys.path.insert(0, os.path.dirname(DIR))

class BaseTestCase(unittest.TestCase):
    '''
    Base Test Case test module
    '''

    def setUp(self):
    trytond.tests.test_tryton.install_module('test')
    
    self.Personaldetails = POOL.get('party.party')
    self.Education = POOL.get('party.education')

class TestTestModule(BaseTestCase):
    '''
    Test Test Module
    '''
    def test_0010_personal_details(self):
        with Transaction().start(DB_NAME, USER, context=CONTEXT):
            self.setup_defaults()
