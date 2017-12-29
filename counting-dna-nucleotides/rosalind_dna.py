#Counting DNA Nucleotides

"""
Given: A DNA string s of length at most 1000 nt.
Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
"""

foo=open("rosalind_dna.txt","r")
str=foo.read()
n={}

for i in str:
	n[i]=str.count(i)

for key in sorted({'A','C','G','T'}):
	print n[key],

foo.close()