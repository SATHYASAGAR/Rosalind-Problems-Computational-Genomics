#Transitions and Transversions

"""
Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).
Return: The transition/transversion ratio R(s1,s2)).
"""

foo = open("rosalind_tran.txt",'r')
strt = foo.read()
seq=strt.strip().split('>')
str = []

        
for s in seq:       #Concatinate all the multiline strings
    if(s!=""):
        all_str=s.split()
        str1=all_str[0]
        str2=''.join(all_str[1:])
        str.append(str2)

firstString = str[0]
secondString = str[1]
transitionCount=0
transversionCount=0
for (i,j) in zip(firstString,secondString):
    if i+j == "AG" or i+j =="GA":
        transitionCount+=1
    if i+j == "CT" or i+j =="TC":
        transitionCount+=1
    if i+j == "AC" or i+j =="CA":
        transversionCount+=1
    if i+j == "GT" or i+j =="TG":
        transversionCount+=1
    if i+j == "AT" or i+j =="TA":
        transversionCount+=1
    if i+j == "GC" or i+j =="CG":
        transversionCount+=1

ratio=transitionCount/(1.0*transversionCount)
print ratio

foo.close()