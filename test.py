import code
import unittest
import random

class TestStringMethods(unittest.TestCase):

    def test(self):
        self.assertEqual(type(code.myFunction(0)), str)
        for i in range(5):
            num = random.randint(1,101)
        self.assertEqual(len(code.myFunction(num)),  num)

if __name__ == '__main__':
    unittest.main()