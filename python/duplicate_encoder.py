'''
http://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python


The goal of this exercise is to convert a string to a new string where each character in the new string is '(' if that character appears only once in the original string, or ')' if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

Examples:

"din" => "((("

"recede" => "()()()"

"Success" => ")())())"

"(( @" => "))((" 

'''

from collections import Counter

def duplicate_encode(word):
    counts = Counter(word.lower())
    return ''.join('(' if counts[c]==1 else ')' for c in word.lower())