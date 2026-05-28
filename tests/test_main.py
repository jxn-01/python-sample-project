import unittest

from main import greet, add_numbers


class TestMain(unittest.TestCase):
    def test_greet_normal(self):
        self.assertEqual(greet("Alice"), "Hello, Alice! Welcome to my GitHub project.")

    def test_greet_empty(self):
        self.assertEqual(greet(""), "Hello, ! Welcome to my GitHub project.")

    def test_add_numbers_positive(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_add_numbers_negative(self):
        self.assertEqual(add_numbers(-1, 1), 0)

    def test_add_numbers_zero(self):
        self.assertEqual(add_numbers(0, 0), 0)


if __name__ == "__main__":
    unittest.main()
