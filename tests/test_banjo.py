import unittest
from banjo import areYouPlayingBanjo

class TestAreYouPlayingBanjo(unittest.TestCase):

    def test_basic_cases(self):
        # Basic test cases
        self.assertEqual(areYouPlayingBanjo("martin"), "martin does not play banjo")
        self.assertEqual(areYouPlayingBanjo("Rikke"), "Rikke plays banjo")
        self.assertEqual(areYouPlayingBanjo("rolf"), "rolf plays banjo")
        self.assertEqual(areYouPlayingBanjo("bravo"), "bravo does not play banjo")
    
    def test_edge_cases(self):
        self.assertEqual(areYouPlayingBanjo("R"), "R plays banjo")        
        self.assertEqual(areYouPlayingBanjo("r"), "r plays banjo")

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            areYouPlayingBanjo(123)

        with self.assertRaises(ValueError):
            areYouPlayingBanjo("")

if __name__ == '__main__':
    unittest.main()