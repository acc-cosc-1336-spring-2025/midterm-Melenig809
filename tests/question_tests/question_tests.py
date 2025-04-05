import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from question_a.question_a import is_prime 
from question_b.question_b import get_day_of_week
from question_c.question_c import get_sum_of_evens
from question_d.question_d import get_miles_per_hour

#question a test
class TestIsPrimeFunction(unittest.TestCase):
    
    def test_is_prime_4(number):
        number.assertFalse(is_prime(4))

    def test_is_prime_5(number):
        number.assertTrue(is_prime(5))  

    def test_is_prime_11(number):
        number.assertTrue(is_prime(11))  

#question b test
class TestGetDayOfTheWeek(unittest.TestCase):
  
    def test_day_of_week_0(day):
        day.assertEqual(get_day_of_week(0), "Error: Invalid number! Please enter a number between 1 and 7.")

    def test_day_of_week_1(day):
        day.assertEqual(get_day_of_week(1), "Monday")

    def test_day_of_week_2(day):
        day.assertEqual(get_day_of_week(2), "Tuesday")

    def test_day_of_week_3(day):
        day.assertEqual(get_day_of_week(3), "Wednesday")

    def test_day_of_week_8(day):
        day.assertEqual(get_day_of_week(8), "Error: Invalid number! Please enter a number between 1 and 7.")

#question c test
class TestGetSumOfEvens(unittest.TestCase):

    def test_get_sum_of_evens_11(number):
        number.assertEqual(get_sum_of_evens(11), 30)  

    def test_get_sum_of_evens_10(number):
        number.assertEqual(get_sum_of_evens(10), 30)  

    def test_get_sum_of_evens_8(number):
        number.assertEqual(get_sum_of_evens(8), 20)

#question d test
class TestGetMilesPerHourFunction(unittest.TestCase):

    def test_get_miles_per_hour(number):
        number.assertAlmostEqual(get_miles_per_hour(32, 60), 19.883872, places=6)

if __name__ == '__main__':
    unittest.main()  





