import unittest

from running_sum import running_sum

class test_running_sum(unittest.TestCase):
    def test_basic_cases(self):
        self.assertEqual(running_sum([3, 1, 2, 10, 1]), [3, 4, 6, 16, 17])
    def test_single_element(self):
        self.assertEqual(running_sum([5]), [5])

    def test_all_zeros(self):
        self.assertEqual(running_sum([0, 0, 0, 0, 0]), [0, 0, 0, 0, 0])

    def test_negative_values(self):
        self.assertEqual(running_sum([-1, -2]), [-1, -3])
        self.assertEqual(running_sum([1, -1, 3, -3]), [1, 0, 3, 0])

    def test_empty_values(self):
        self.assertEqual(running_sum([]), [])

if __name__ == '__main__':
    unittest.main()