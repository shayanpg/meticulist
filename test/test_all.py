import unittest
from src import list


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)
        self.assertEqual(list.to_test(), 7)


if __name__ == '__main__':
    unittest.main()
