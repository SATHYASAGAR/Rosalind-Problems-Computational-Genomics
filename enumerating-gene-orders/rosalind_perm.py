#Enumerating Gene Orders

import itertools

foo = open("rosalind_perm.txt","r")
number = foo.read().strip();

permutations_of_n = set(itertools.permutations(range(int(number)+1)[1:]))

print len(permutations_of_n) 

for x in permutations_of_n:
    for k in x:
        print str(k),
    print

    
    