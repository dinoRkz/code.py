#!/usr/bin/python3
import unittest
from collections import Counter

def duplicate_encode(word):
    word = word.lower()
    new_string = ''
    count = Counter(word)
    for x in word:
        if count[x] == 1:
            new_string += '('
        else:
            new_string += ')'
    return new_string

class Test(unittest.TestCase):
	def test_cases(self):
		self.assertEqual(duplicate_encode('din'),'(((')
		self.assertEqual(duplicate_encode('recede'),'()()()')
		self.assertEqual(duplicate_encode('Success'),')())())')
		self.assertEqual(duplicate_encode('(( @'),'))((')

if __name__ == "__main__":
    unittest.main()