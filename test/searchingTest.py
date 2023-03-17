import unittest
from searchMethods import searching

arrayLinear = [[4, 18, -1, 0, 34, 7, 6, 15, 87, 10], 25, 34]

arrayBinary = [[4, 2, 37, 90, 65, 18, 3, 37, 115, 15], 10, 37]

arrayTernary = [[82, 0, 1, 23, 13, 78, 45, 32, 69, 15], 2, 15]


class AlgorithmsTests(unittest.TestCase):

    def test_linear_search_not_in_the_list(self):
        self.assertFalse(searching.linearSearch(arrayLinear[0], arrayLinear[1]))

    def test_binary_search_not_in_the_list(self):
        self.assertFalse(searching.linearSearch(arrayBinary[0], arrayBinary[1]))

    def test_ternary_search_not_in_the_list(self):
        self.assertFalse(searching.linearSearch(arrayTernary[0], arrayTernary[1]))

    def test_linear_search_in_the_list(self):
        self.assertTrue(searching.linearSearch(arrayLinear[0], arrayLinear[2]))

    def test_binary_search_in_the_list(self):
        self.assertTrue(searching.linearSearch(arrayBinary[0], arrayBinary[2]))

    def test_ternary_search_in_the_list(self):
        self.assertTrue(searching.linearSearch(arrayTernary[0], arrayTernary[2]))


if __name__ == '__main__':
    unittest.main()
