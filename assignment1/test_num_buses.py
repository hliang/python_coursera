import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    # Add your test methods for a1.num_buses here.
    def test_num_buses_zero(self):
        """no people, no bus needed"""
        actual = a1.num_buses(0)
        expected = 0
        self.assertEqual(actual, expected)
    
    def test_num_buses_all_full(self):
        """all people fit exactly into the bus. all seats occuppied, no empty seats"""
        actual = a1.num_buses(50)
        expected = 1
        self.assertEqual(actual, expected)

    def test_num_buses_partial_1(self):
        """some but not all seats occuppied, i.e. bus is not full"""
        actual = a1.num_buses(51)
        expected = 2
        self.assertEqual(actual, expected)

    def test_num_buses_partial_2(self):
        """some but not all seats occuppied, i.e. bus is not full"""
        actual = a1.num_buses(125)
        expected = 3
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(exit=False)
