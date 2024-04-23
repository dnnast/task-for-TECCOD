# tests are generated using Bito AI

from task_1 import uniqueNumbers
import unittest

class TestUniqueNumbers(unittest.TestCase):
    
    def test_positive_case(self):
        numbers = [1, 2, 13, 4, 5, 0, 2, 2, 5, 5, 46, 3, 4, 6, 9]
        self.assertEqual(uniqueNumbers(numbers), [0, 1, 2, 3, 4, 5, 6, 9, 13, 46])
    
    def test_empty_list(self):
        numbers = []
        self.assertEqual(uniqueNumbers(numbers), [])
    
    def test_single_element_list(self):
        numbers = [5]
        self.assertEqual(uniqueNumbers(numbers), [5])
        
    def test_all_duplicate_elements(self):
        numbers = [2, 2, 2, 2, 2]
        self.assertEqual(uniqueNumbers(numbers), [2])
    
    def test_negative_numbers(self):
        numbers = [-1, -5, -1, -5, -3, -3]
        self.assertEqual(uniqueNumbers(numbers), [-5, -3, -1])
        
if __name__ == '__main__':
    unittest.main()