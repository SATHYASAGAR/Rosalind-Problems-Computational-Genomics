#Reconstruct a String from its Genome Path

"""
Given: A sequence of k-mers Pattern1, ... , Patternn such that the last k - 1 symbols of Patterni are equal to the first k - 1 symbols of Patterni+1 for i from 1 to n-1.
Return: A string Text of length k+n-1 where the i-th k-mer in Text is equal to Patterni for all i.
"""

foo=open("rosalind_ba3b.txt","r")
kmerSequences=foo.read().strip().splitlines()

i=0
outputString=""

for kmerSequence in kmerSequences:
    if(i == 0):
        outputString+=kmerSequence
    else:
        outputString+=kmerSequence[len(kmerSequence)-1]
    i+=1

print outputString