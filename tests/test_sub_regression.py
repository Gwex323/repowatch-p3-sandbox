import unittest

from sub import sub


class SubRegression(unittest.TestCase):
    def test_existing_issue_contract(self):
        for left, right, expected in [(5, 2, 3), (2, 5, -3), (0, 0, 0)]:
            with self.subTest(left=left, right=right):
                self.assertEqual(sub(left, right), expected)


if __name__ == '__main__':
    unittest.main()
