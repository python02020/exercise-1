import ex1
import unittest
import random

class TestStringMethods(unittest.TestCase):

    def test(self):
        self.assertEqual(type(ex1.makeString(0)), str)
        for i in range(5):
            num = random.randint(1,101)
            self.assertEqual(len(ex1.makeString(num)),  num)
        self.assertRaises(Exception, ex1.makeString, -1)

if __name__ == '__main__':
    unittest.main()