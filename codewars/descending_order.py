#!/usr/bin/python3
import unittest

def Descending_Order(num):
    num_list = []
    str_num = str(num)
    # To convert string into list of chars 
    for i in range(len(str_num)):
        num_list.append(str_num[i])
    # sort the list and convert it back to string
    sorted_str = ''.join(sorted(num_list, reverse=True))
    return int(sorted_str)

class Test(unittest.TestCase):
	def test_cases(self):
		self.assertEqual(Descending_Order(15),51)
		self.assertEqual(Descending_Order(21445),54421)
		self.assertEqual(Descending_Order(145263),654321)
		self.assertEqual(Descending_Order(1254859723),9875543221)
		
if __name__ == "__main__":
    unittest.main()