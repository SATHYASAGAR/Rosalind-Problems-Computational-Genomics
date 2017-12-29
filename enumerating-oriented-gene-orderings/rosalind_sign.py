#Enumerating Oriented Gene Orders

import itertools

foo = open("rosalind_sign.txt","r")
number = foo.read().strip();

lst = range(-int(number),int(number)+1)
lst.remove(0)
lst_1=[[]]
p = set(itertools.permutations(lst,int(number)))
list_1 = list(p)

#list2 = [x for x in lst_1 if x != []]

gene_orders =[]
            
for element in list_1:
    flag=0
    for j in element:
        if ((j in element) & ((j*-1) in element)):
            flag = 1
            break
    if flag == 0:
        gene_orders.append(list(element))
print len(gene_orders)
for i in gene_orders:
    for j in i:
        print j,
    print
    
    