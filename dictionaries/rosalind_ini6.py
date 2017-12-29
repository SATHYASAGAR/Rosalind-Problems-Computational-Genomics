#Dictionaries

"""
Given: A string s of length at most 10000 letters
Return:  The number of occurrences of each word in s, where words are separated by spaces. Words are case-sensitive, and the lines in the output can be in any order.
"""

from collections import defaultdict

foo=open("rosalind_ini6.txt","r")
str=foo.read()
d=defaultdict(int)

for i in str.strip().split(' '):
    d[i]+=1

for word,count in d.items():
    print word,count
    
foo.close()