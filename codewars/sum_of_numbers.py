#!/usr/bin/python3
import unittest

# Method 1
def get_sum_1(a,b):
    sum = 0
    if(a == b):
        return a
    else:
        for i in range(min(a,b),max(a,b)+1):
            sum = sum + i
        return sum

# Method 2
def get_sum_2(a,b):
    return sum(range(min(a,b), max(a,b)+1))

class Test(unittest.TestCase):
    def test_cases_get_sum_1(self):
        self.assertEqual(get_sum_1(0,1),1)
        self.assertEqual(get_sum_1(1,2),3)
        self.assertEqual(get_sum_1(5,-1),14)
        self.assertEqual(get_sum_1(505,4),127759)
        self.assertEqual(get_sum_1(321,123),44178)
        self.assertEqual(get_sum_1(0,-1),-1)
        self.assertEqual(get_sum_1(-50,0),-1275)
        self.assertEqual(get_sum_1(-1,-5),-15)
        self.assertEqual(get_sum_1(-5,-5),-5)
        self.assertEqual(get_sum_1(-505,4),-127755)
        self.assertEqual(get_sum_1(-321,123),-44055)
        self.assertEqual(get_sum_1(0,0),0)
        self.assertEqual(get_sum_1(-5,-1),-15)
        self.assertEqual(get_sum_1(5,1),15)
        self.assertEqual(get_sum_1(-17,-17),-17)
        self.assertEqual(get_sum_1(17,17),17)

    def test_cases_get_sum_2(self):
        self.assertEqual(get_sum_2(0,1),1)
        self.assertEqual(get_sum_2(1,2),3)
        self.assertEqual(get_sum_2(5,-1),14)
        self.assertEqual(get_sum_2(505,4),127759)
        self.assertEqual(get_sum_2(321,123),44178)
        self.assertEqual(get_sum_2(0,-1),-1)
        self.assertEqual(get_sum_2(-50,0),-1275)
        self.assertEqual(get_sum_2(-1,-5),-15)
        self.assertEqual(get_sum_2(-5,-5),-5)
        self.assertEqual(get_sum_2(-505,4),-127755)
        self.assertEqual(get_sum_2(-321,123),-44055)
        self.assertEqual(get_sum_2(0,0),0)
        self.assertEqual(get_sum_2(-5,-1),-15)
        self.assertEqual(get_sum_2(5,1),15)
        self.assertEqual(get_sum_2(-17,-17),-17)
        self.assertEqual(get_sum_2(17,17),17)

if __name__ == "__main__":
    unittest.main()