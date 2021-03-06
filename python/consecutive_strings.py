'''
http://www.codewars.com/kata/consecutive-strings/train/python


You are given an array strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.

#Example: longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"

n being the length of the string array, if n = 0 or k > n or k <= 0 return "".


'''


def longest_consec(strarr, k):
    
    if k > len(strarr) or len(strarr) < 1 or k <= 0:
        return ""
    
    max_str = ''
    
    for i in range(len(strarr)):
        this_str = ''.join(strarr[i:i+k])
        if len(this_str) > len(max_str):
            max_str = this_str
    
    return max_str