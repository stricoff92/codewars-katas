
'''

http://www.codewars.com/kata/find-the-odd-int/train/python


Given an array, find the int that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

'''


from collections import Counter

def find_it(seq):
    for k, v in Counter(seq).items():
        if v % 2:
            return k