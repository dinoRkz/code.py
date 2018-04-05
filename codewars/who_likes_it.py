#!/usr/bin/python3
import unittest

# Method 1
def likes_1(names):
    ret = ""
    if (len(names) == 0):
        ret = "no one likes this"
    elif (len(names) == 1):
        ret = str(names[0]) + " likes this"
    elif (len(names) > 1 and len(names) < 4):
        for i in range(0, len(names) - 1):
            ret = ret + names[i] + ", "
        ret = ret[:-2]
        ret = ret + " and " + str(names[len(names) - 1]) + " like this"
    else:
        for i in range(0, 2):
            ret = ret + names[i] + ", "
        ret = ret[:-2]
        ret = ret + " and " + str(len(names)-2) + " others like this"
    return ret

# Method 2
def likes_2(names):
    n = len(names)
    # min(4, n) - to select the index of dictionary
    # *names[:3] to replace {} with names in order
    return {
    0: 'no one likes this',
    1: '{} likes this', 
    2: '{} and {} like this', 
    3: '{}, {} and {} like this', 
    4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)

class Test(unittest.TestCase):
    def test_cases_likes_1(self):
        self.assertEqual(likes_1([]), 'no one likes this')
        self.assertEqual(likes_1(['Peter']), 'Peter likes this')
        self.assertEqual(likes_1(['Jacob', 'Alex']), 'Jacob and Alex like this')
        self.assertEqual(likes_1(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
        self.assertEqual(likes_1(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')

    def test_cases_likes_2(self):
        self.assertEqual(likes_2([]), 'no one likes this')
        self.assertEqual(likes_2(['Peter']), 'Peter likes this')
        self.assertEqual(likes_2(['Jacob', 'Alex']), 'Jacob and Alex like this')
        self.assertEqual(likes_2(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
        self.assertEqual(likes_2(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')

if __name__ == "__main__":
    unittest.main()