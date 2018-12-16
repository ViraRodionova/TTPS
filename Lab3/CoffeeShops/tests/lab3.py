import unittest
from Main import main

class UnitTests(unittest.TestCase):
    def test_1(self):
        filename = '../inputs/input1'
        self.assertEqual(
            {
                1: {
                    'shops': 3,
                    'positions': [
                        [3, 4]
                    ]
                },
                2: {
                    'shops': 4,
                    'positions': [
                        [1, 3],
                        [2, 2]
                    ]
                },
                4: {
                    'shops': 5,
                    'positions': [
                        [1, 3],
                        [1, 4],
                        [2, 2],
                        [2, 3],
                        [3, 1],
                        [3, 2],
                        [4, 2]
                    ]
                }
            },
            main(filename)
        )

    def test_3(self):
        filename = '../inputs/input3'
        self.assertEqual(
            {
                2: {
                    'shops': 3,
                    'positions': [
                        [3, 3],
                        [4, 2]
                    ]
                },
                4: {
                    'shops': 4,
                    'positions': [
                        [1, 3],
                        [2, 3],
                        [2, 4],
                        [3, 2],
                        [3, 3],
                        [3, 4],
                        [3, 5],
                        [4, 3],
                        [4, 4]
                    ]
                }
            },
            main(filename)
        )

if __name__ == '__main__':
    unittest.main()