#Creating a Distance Matrix

import numpy as np

def get_strs_from_input(file_name,mode):
    """Function to get the strings from a file which is in FASTA format.
    
    Keyword Argument:
    file_name -- name of the file
    mode -- mode in which the file needs to be opened
    
    Return Value:
    Returns the strings.
    """
    foo = open(file_name,mode)                   
    seq = foo.read().split(">")            
    strs = []
    for s in seq:
        if(s!=""):
            strings=s.split()
            s_1=strings[0]
            s_2=''.join(strings[1:])
            strs.append(s_2)    
    return strs

def hamming_distance(s,t):
    """Return the hamming distance between two DNA strings
    
    Keyword Argument:
    s -- first dna string
    t -- second dna string
    
    Return Value:
    Hamming distance between s and t
    """
    hamming_distance=0
    for i in range(len(t)):
        if s[i]<>t[i]:
            hamming_distance+=1
    return hamming_distance
    
def main():
    """main function to create the distance matrix"""
    strs = get_strs_from_input("rosalind_pdst.txt",'r') 
    distance_matrix = [[hamming_distance(strs[x],strs[y])/(len(strs[x])*1.0) for x in range(len(strs))] for y in range(len(strs))]
    for row in distance_matrix:
        for element in row:
            print "{0:0.5f}".format(element),
        print
if __name__ =='__main__':
    main()