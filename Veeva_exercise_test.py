__author__ = 'nickyuan'

import unittest
from Veeva_exercise import dayofyear, leap_year


class TestCase(unittest.TestCase):
    '''Test for leap year and dayofyear'''

    def test_is_leapyear(self):
        self.assertTrue(leap_year(2016))
        self.assertTrue(leap_year(2000))
        self.assertFalse(leap_year(1900))
        self.assertFalse(leap_year(2009))
        self.assertFalse(leap_year(-1))

    def test_dayofyear(self):
        self.assertEqual(63, dayofyear(2016, 3, 3))
        self.assertEqual(62, dayofyear(2017, 3, 3))


if __name__ == '__main__':
    unittest.main()
