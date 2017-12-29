#Transcribing DNA into RNA

"""
Given: A DNA string t having length at most 1000 nt.
Return: The transcribed RNA string of t.
"""

foo=open("rosalind_rna.txt","r")		#Read input from a file
t=foo.read()

transcribed_rna_str=t.replace('T','U') 	#Replace all occurrences of 'T' in t with 'U' to get the transcribed RNA string of t.

print transcribed_rna_str

foo.close()