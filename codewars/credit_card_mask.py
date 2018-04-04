#!/usr/bin/python3
import unittest

def maskify(cc):
	return (len(cc) - 4) * "#" + cc[-4:]

class Test(unittest.TestCase):
	def test_cases(self):
		self.assertEqual(maskify(''),'')
		self.assertEqual(maskify('123'),'123')
		self.assertEqual(maskify('SF$SDfgsd2eA'),'########d2eA')
		self.assertEqual(maskify('4556364607935616'),'############5616')
		self.assertEqual(maskify('64607935616'),'#######5616')
		self.assertEqual(maskify('Skippy'),'##ippy')
		self.assertEqual(maskify('Nananananananananananananananana Batman!'),'####################################man!')
		
if __name__ == "__main__":
    unittest.main()