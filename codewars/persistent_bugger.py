#!/usr/bin/python3
import unittest
import functools
import operator # This package has standard operators like  as functions

def persistence(n):
    count = 0
    n_str = str(n)
    while(len(n_str) > 1):
        count += 1
        # convert each char of the list to number and multiply
        # convert that number back to string for next iteration
        n_str = str(functools.reduce(operator.mul, [int(x) for x in n_str]))
    return count

class Test(unittest.TestCase):
	def test_cases(self):
		self.assertEqual(persistence(39),3)
		self.assertEqual(persistence(4),0)
		self.assertEqual(persistence(25),2)
		self.assertEqual(persistence(999),4)
		self.assertEqual(persistence(387456),2)
		self.assertEqual(persistence(245703),1)

if __name__ == "__main__":
    unittest.main()