#Inferring mRNA from Protein

"""
Given: A protein string of length at most 1000 a.
Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. 
(Don't neglect the importance of the stop codon in protein translation.)
"""

foo=open("rosalind_mrna.txt","r")
protein_str=foo.read().strip()
codon_freq = {'A':4,'R':6,'N':2,'D':2,'C':2,'Q':2,'E':2,'G':4,'H':2,'I':3,'L':6,'K':2,'M':1,'F':2,'P':4,'S':6,'T':4,'W':1,'Y':2,'V':4,'*':3}

total_rna_str=1

for i in protein_str:				#Compute total number of RNA strings not considering the stop codon
	total_rna_str*=codon_freq[i]	
	
total_rna_str*=codon_freq['*']		#Considering the stop codon
total_rna_str=total_rna_str%1000000

print total_rna_str
foo.close()