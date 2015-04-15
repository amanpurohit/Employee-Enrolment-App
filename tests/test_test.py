import sys
import os
import unittest
from datetime import date

import trytond.tests.test_tryton
from trytond.tests.test_tryton import POOL, DB_NAME, USER, CONTEXT
from trytond.transaction import Transaction

DIR = os.path.abspath(os.path.normpath(os.path.join(
    __file__, '..', '..', '..', '..', '..', 'trytond'
)))
if os.path.isdir(DIR):
    sys.path.insert(0, os.path.dirname(DIR))


class TestTestModule(unittest.TestCase):

    def setUp(self):
        trytond.tests.test_tryton.install_module('test')

        self.Party = POOL.get('party.party')
        self.Personaldetails = POOL.get('party.party')
        self.Education = POOL.get('party.education')

    """
    Test Test Module
    """

    def test_0010_personal_details(self):
            # Create Party
        with Transaction().start(DB_NAME, USER, context=CONTEXT):
            party, = self.Party.create([{
                'name': 'Openlabs',
                'gender': 'undefined',
                'date_of_birth': date(1990, 4, 11),
                'place_of_birth': 'New Delhi',
                'pan_card_number': '1234567890',
                'marital_status': 'single',
                'education': [('create', [{
                    'degree': 'B.Tech',
                    'stream': 'computer science',
                    'grade': 'B+',
                    'university': 'indraprastha university',
                    'year_of_completion': '2015',
                }])],
            }])
            self.assertTrue(party)

    def test_0020_invalid_date_of_birth(self):
            # Create Party
        with Transaction().start(DB_NAME, USER, context=CONTEXT):
            with self.assertRaises(ValueError):
                party, = self.Party.create([{
                    'name': 'Openlabs',
                    'gender': 'undefined',
                    'date_of_birth': date(2015, 4, 11),
                    'place_of_birth': 'New Delhi',
                    'pan_card_number': '1234567890',
                    'marital_status': 'single',
                    'education': [('create', [{
                        'degree': 'B.Tech',
                        'stream': 'computer science',
                        'grade': 'B+',
                        'university': 'indraprastha university',
                        'year_of_completion': '2015',
                    }])],
                }])

    def test_0030_gender_required(self):
            # Create Party
        with Transaction().start(DB_NAME, USER, context=CONTEXT):
            party, = self.Party.create([{
                'name': 'Openlabs',
                'date_of_birth': date(1990, 4, 11),
                'place_of_birth': 'New Delhi',
                'pan_card_number': '1234567890',
                'marital_status': 'single',
                'education': [('create', [{
                    'degree': 'B.Tech',
                    'stream': 'computer science',
                    'grade': 'B+',
                    'university': 'indraprastha university',
                    'year_of_completion': '2015',
                }])],
            }])
            self.assertEqual(party.gender, 'male')


def suite():
    """
    Define Suite
    """
    test_suite = trytond.tests.test_tryton.suite()
    test_suite.addTests(
        unittest.TestLoader().loadTestFromTestCase(TestTestModule)
    )
    return test_suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=1).run(suite())
