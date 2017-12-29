#Find the Reverse Complement of a String

"""
Given: A DNA string Pattern.
Return: Pattern', the reverse complement of Pattern.
"""

foo=open("rosalind_ba1c.txt","r")
s=foo.read()
rev_complement=''

for i in s:
	if i=='A':
		rev_complement+='T'
		
	elif i=='T':
		rev_complement+='A'
		
	elif i=='C':
		rev_complement+='G'
		
	elif i=='G':
		rev_complement+='C'
			
	else:
		rev_complement+=i

rev_complement=rev_complement[::-1]
print rev_complement
foo.close()