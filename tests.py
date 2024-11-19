import unittest
from sndhdr import tests
# https://docs.python.org/3/tutorial/errors.html

# Feature 3aii

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # This is an example


if __name__ == '__main__':
    unittest.main() # Runs all tests
