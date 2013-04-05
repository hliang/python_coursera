import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    # Add your test methods for a1.swap_k here.
    def test_swap_empty_list(self):
        """an empty list stays the same, i.e. still an empty list"""
        nums = []
        nums_expected = []
        a1.swap_k(nums, 2)
        self.assertEqual(nums, nums_expected)

    def test_swap_len_one(self):
        """a list with only one element should stay the same"""
        nums = [5]
        nums_expected = [5]
        a1.swap_k(nums, 1)
        self.assertEqual(nums, nums_expected)

    def test_swap_len_one_k_too_long(self):
        """when k is larger than len//2, list should stay the same, because it cannot be swapped"""
        nums = [5]
        nums_expected = [5]
        a1.swap_k(nums, 3)
        self.assertEqual(nums, nums_expected)

    def test_swap_k_too_long(self):
        """when k is larger than len//2, list should stay the same, because it cannot be swapped"""
        nums = [1,2,3,4,5]
        nums_expected = [1,2,3,4,5]
        a1.swap_k(nums, 3)
        self.assertEqual(nums, nums_expected)

    def test_swap_negative_k(self):
        """when k is negative, list should stay the same, because it cannot be swapped"""
        nums = [1,2,3,4,5]
        nums_expected = [1,2,3,4,5]
        a1.swap_k(nums, -2)
        self.assertEqual(nums, nums_expected)

    def test_swap_zero_move(self):
        """ k = 0, no swap needed, list stays the same """
        nums = [1, 2, 3, 4, 5]
        nums_expected = [1, 2, 3, 4, 5]
        a1.swap_k(nums, 0)
        self.assertEqual(nums, nums_expected)

    def test_swap_odd_len(self):
        """ odd length """
        nums = [1, 2, 3, 4, 5]
        nums_expected = [4, 5, 3, 1, 2]
        a1.swap_k(nums, 2)
        self.assertEqual(nums, nums_expected)

    def test_swap_even_len(self):
        """ odd length """
        nums = [1, 2, 3, 4, 5, 6]
        nums_expected = [4, 5, 6, 1, 2, 3]
        a1.swap_k(nums, 3)
        self.assertEqual(nums, nums_expected)



if __name__ == '__main__':
    unittest.main(exit=False)
