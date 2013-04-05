import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    # Add your test methods for a1.stock_price_summary here.
    def test_stock_empty(self):
        """empty list"""
        price_changes = []
        expected = (0, 0)
        actual = a1.stock_price_summary(price_changes)
        self.assertEqual(actual, expected)

    def test_stock_only_one(self):
        """list of one element"""
        price_changes = [0.3]
        expected = (0.3, 0)
        actual = a1.stock_price_summary(price_changes)
        self.assertEqual(actual, expected)

    def test_stock_all_zero(self):
        """list of all zero elements"""
        price_changes = [0, 0, 0, 0, 0]
        expected = (0, 0)
        actual = a1.stock_price_summary(price_changes)
        self.assertEqual(actual, expected)

    def test_stock_all_pos(self):
        """list of all positive or zero values, i.e. without negative values"""
        price_changes = [0.01, 0.02, 0.03, 0.14, 0, 0, 0.15, 0.06]
        expected = (0.41, 0)
        actual = a1.stock_price_summary(price_changes)
        self.assertEqual(actual, expected)

    def test_stock_all_neg(self):
        """list of all negative values, i.e. without positive values"""
        price_changes = [-0.01, -0.02, -0.03, -0.14, -0, -0, -0.15, -0.06]
        expected = (0, -0.41)
        actual = a1.stock_price_summary(price_changes)
        self.assertEqual(actual, expected)

    def test_stock_pos_and_neg(self):
        """list of mix of positive, negative and zero values"""
        price_changes = [0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01]
        expected = (0.14, -0.17)
        actual = a1.stock_price_summary(price_changes)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(exit=False)
