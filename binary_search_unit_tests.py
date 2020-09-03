import unittest
from binary_search_v3 import binary_search, linear_search


class TestBinarySearch(unittest.TestCase):
    def test_small(self):
        for (keys, query) in [
            ([1, 2, 3], 1),
            ([4, 5, 6], 7),
            ([5, 6, 8, 10, 11, 20], 10)
        ]:
            print(linear_search(keys, query))
            print(binary_search(keys, query, len(keys)-1, 0))
            self.assertEqual(
                linear_search(keys, query),
                binary_search(keys, query, len(keys)-1, 0)
            )

    def test_large(self):
        for (keys, query, answer) in [
            (list(range(10 ** 4)), 10 ** 4, -1),
            (list(range(1, 10 ** 4)), 49, 47),
            (list(range(10 ** 4)), 239, 239),
        ]:
            self.assertEqual(binary_search(keys, query, len(keys)-1, 0), answer)


if __name__ == '__main__':
    unittest.main()
