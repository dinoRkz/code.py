#!/usr/bin/python3
import unittest
import math

def is_square(n):  
    if(n >= 0 ):
        return (n**0.5 == int(n**0.5))
    else:
        return 0

class Test(unittest.TestCase):
	def test_cases(self):
		self.assertEqual(is_square(-1),0)
		self.assertEqual(is_square(3),0)
		self.assertEqual(is_square(4),1)
		self.assertEqual(is_square(256),1)
		self.assertEqual(is_square(12332),0)
		self.assertEqual(is_square(245703),0)

if __name__ == "__main__":
    unittest.main()