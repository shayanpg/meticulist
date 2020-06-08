import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    """ To run all tests
    
        python -m unittest discover test 
        
        from meticulist directory
    """
    unittest.main()
