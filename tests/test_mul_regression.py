import unittest

from mul import mul


class MulRegression(unittest.TestCase):
    def test_existing_issue_contract(self):
        for left, right, expected in [(2, 3, 6), (2, 0, 0), (-2, 3, -6)]:
            with self.subTest(left=left, right=right):
                self.assertEqual(mul(left, right), expected)


if __name__ == '__main__':
    unittest.main()
