#Strings and lists

"""
Given: A string s of length at most 200 letters and four integers a, b, c and d.
Return: The slice of this string from indices a through b and c through d (with space in between), inclusively. In other words, we should include elements s[b] and s[d] in our slice.
"""

foo=open("rosalind_ini3.txt","r")
str=foo.read()

letters = str.split('\n')[0]
numbers = str.split('\n')[1].split()

firstSlice = letters[int(numbers[0]):int(numbers[1])+1]
secondSlice = letters[int(numbers[2]):int(numbers[3])+1]

print  firstSlice,secondSlice