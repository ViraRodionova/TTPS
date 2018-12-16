import unittest
from Main import main
from Errors import *

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

    def test_2(self):
        filename = '../inputs/input2'
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

    def test_min_values(self):
        filename = '../inputs/input3'
        self.assertEqual(
            {
                0: {
                    'shops': 0,
                    'positions': [
                        [1, 1]
                    ]
                }
            },
            main(filename)
        )

    def test_dx_out_of_range_min(self):
        filename = '../inputs/input4'
        self.assertRaises(
            DxOutOfRange,
            main, filename
        )

    def test_dx_out_of_range_max(self):
        filename = '../inputs/input5'
        self.assertRaises(
            DxOutOfRange,
            main, filename
        )

    def test_dy_out_of_range_min(self):
        filename = '../inputs/input6'
        self.assertRaises(
            DyOutOfRange,
            main, filename
        )

    def test_dy_out_of_range_max(self):
        filename = '../inputs/input7'
        self.assertRaises(
            DyOutOfRange,
            main, filename
        )

    def test_n_out_of_range_min(self):
        filename = '../inputs/input8'
        self.assertRaises(
            NOutOfRange,
            main, filename
        )

    def test_n_out_of_range_max(self):
        filename = '../inputs/input9'
        self.assertRaises(
            NOutOfRange,
            main, filename
        )

    def test_q_out_of_range_min(self):
        filename = '../inputs/input10'
        self.assertRaises(
            QOutOfRange,
            main, filename
        )

    def test_q_out_of_range_max(self):
        filename = '../inputs/input11'
        self.assertRaises(
            QOutOfRange,
            main, filename
        )

    def test_shop_out_of_range(self):
        filename = '../inputs/input12'
        self.assertRaises(
            ShopCoordinatesOutOfRange,
            main, filename
        )

    def test_invalid_shops_count(self):
        filename = '../inputs/input13'
        self.assertRaises(
            Exception,
            main, filename
        )

    def test_invalid_shops_count_2(self):
        filename = '../inputs/input14'
        self.assertRaises(
            Exception,
            main, filename
        )

    def test_dublicate_shops_count(self):
        filename = '../inputs/input15'
        self.assertRaises(
            DublicateShops,
            main, filename
        )

    def test_invalid_queries_count(self):
        filename = '../inputs/input16'
        self.assertRaises(
            Exception,
            main, filename
        )


if __name__ == '__main__':
    unittest.main()