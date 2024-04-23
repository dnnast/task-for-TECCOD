# some of the tests are generated using Bito AI

import unittest
from task_2 import primeNumbers

class TestPrimeNumbersFunction(unittest.TestCase):

    def test_positive_case(self):
        self.assertEqual(primeNumbers(1, 10), [2, 3, 5, 7])

    def test_negative_case(self):
        with self.assertRaises(ValueError):
            primeNumbers('d', 10)

    def test_reversed_order_range(self):
        self.assertEqual(primeNumbers(20, 10), [11, 13, 17, 19])

    def test_large_range(self):
        self.assertEqual(primeNumbers(1, 100), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])

if __name__ == '__main__':
    unittest.main()