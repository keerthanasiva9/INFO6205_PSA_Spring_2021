#Valid Anagram

#Given two strings s and t, return true if t is an anagram of s, and false otherwise.

#Input: s = "anagram", t = "nagaram"
#Output: true

#Input: s = "rat", t = "car"
#Output: false

import collections
from collections import Counter
def valid_anagram(s,t):
    count_s = collections.Counter(s)
    count_t = collections.Counter(t)
    if count_s.items() == count_t.items():
        return True
    return False


if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    print("Input strings are:",s,"and",t)
    print(valid_anagram(s,t))
