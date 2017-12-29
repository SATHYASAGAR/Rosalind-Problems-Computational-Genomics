#Generate the k-mer Composition of a String

"""
Given: An integer k and a string Text.
Return: Compositionk(Text) (the k-mers can be provided in any order).
"""

foo=open("rosalind_ba3a.txt","r")
str=foo.read().strip().splitlines()

k = int(str[0]);
string = str[1]

composition = [];

for i in range(0,len(string)-k+1):
    composition.insert(0,string[i:i+k])
    
composition.sort()
for kmerSubstring in composition:
    print kmerSubstring
    
foo.close()