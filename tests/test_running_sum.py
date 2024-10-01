import unittest

from running_sum import running_sum

class TestRunningSum(unittest.TestCase):
    def test_basic_cases(self):
        self.assertEqual(running_sum([3, 1, 2, 10, 1]), [3, 4, 6, 16, 17])
        self.assertEqual(running_sum([0, 0, 0, 0, 0]), [0, 0, 0, 0, 0])
        self.assertEqual(running_sum([-1, -2]), [-1, -3])
        self.assertEqual(running_sum([1, -1, 3, -3]), [1, 0, 3, 0])


    def test_single_element(self):
        self.assertEqual(running_sum([5]), [5])

    def test_empty_values(self):
        with self.assertRaises(ValueError):
            running_sum([])
    
    def test_not_integer_list(self):
        with self.assertRaises(TypeError):
            running_sum([1, 2.5, 3])
        
        with self.assertRaises(TypeError):
            running_sum([1, "23", 3])
        
        with self.assertRaises(TypeError):
            running_sum([1, 11, "hi"])

if __name__ == '__main__':
    unittest.main()