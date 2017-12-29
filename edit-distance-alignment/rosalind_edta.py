#Edit Distance Alignment

from numpy import zeros
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

def find_edit_distance(string1,string2):
    """Function to find the edit distance matrix between two protein strings.
    
    Keyword Argument:
    string1 -- first protein string
    string2 -- second protein string
    
    Return Value:
    Returns the edit distance matrix between two strings.
    """
    M=zeros((len(string1)+1,len(string2)+1), dtype=int)
    for s_index in xrange(1,len(string1)+1):
        M[s_index][0]=s_index
    for t_index in xrange(1,len(string2)+1):
        M[0][t_index]=t_index
    for s_index in xrange(1,len(string1)+1):
        for t_index in xrange(1,len(string2)+1):
            if(string1[s_index-1]!=string2[t_index-1]):
                M[s_index][t_index] = min(M[s_index - 1][t_index] + 1, M[s_index][t_index - 1] + 1, M[s_index - 1][t_index - 1] + 1)
            else:
                M[s_index][t_index] = M[s_index - 1][t_index - 1]
    return M

def edit_distance_alignment(M,s,t):
    """Function to get the edit distance alignment of two strings.
    
    Keyword Argument:
    M -- matrix formed for finding the edit distance
    s -- first string
    t -- second string
    
    Return Value:
    Returns the edit distance and augmented strings of s and t.
    """
    s_index=len(s)
    t_index=len(t)
    augmented_string_s=""
    augmented_string_t=""
    while(s_index>0 and t_index>0):
        if s[s_index-1]==t[t_index-1]: 
            augmented_string_s+=s[s_index-1]
            augmented_string_t+=t[t_index-1]
            s_index=s_index-1
            t_index=t_index-1
            continue
        if min(M[s_index-1][t_index-1],M[s_index][t_index-1],M[s_index-1][t_index])==M[s_index-1][t_index-1]:
            if min(M[s_index-1][t_index-1],M[s_index][t_index-1],M[s_index-1][t_index])==M[s_index][t_index-1]: 
                augmented_string_s+='-'
                augmented_string_t+=t[t_index-1]
                t_index=t_index-1
                continue
        if min(M[s_index-1][t_index-1],M[s_index][t_index-1],M[s_index-1][t_index])==M[s_index-1][t_index-1]: 
            if min(M[s_index-1][t_index-1],M[s_index][t_index-1],M[s_index-1][t_index])==M[s_index-1][t_index]:
                augmented_string_s+=s[s_index-1]
                augmented_string_t+='-'
                s_index=s_index-1
                continue
        if min(M[s_index-1][t_index-1],M[s_index][t_index-1],M[s_index-1][t_index])==M[s_index-1][t_index-1]: 
            augmented_string_s+=s[s_index-1]
            augmented_string_t+=t[t_index-1]
            s_index=s_index-1
            t_index=t_index-1
            continue
        if min(M[s_index-1][t_index-1],M[s_index][t_index-1],M[s_index-1][t_index])==M[s_index][t_index-1]: 
            augmented_string_s+='-'
            augmented_string_t+=t[t_index-1]
            t_index=t_index-1
            continue
        if min(M[s_index-1][t_index-1],M[s_index][t_index-1],M[s_index-1][t_index])==M[s_index-1][t_index]:
            augmented_string_s+=s[s_index-1]
            augmented_string_t+='-'
            s_index=s_index-1
            continue
                
    return [M[len(s)][len(t)],augmented_string_s[::-1],augmented_string_t[::-1]]        
    
def main():
    """main function to get the edit distance Alignment"""
    strs = get_strs_from_input("rosalind_edta.txt",'r')
    M = find_edit_distance(strs[0],strs[1])
    output = edit_distance_alignment(M,strs[0],strs[1]);
    print output[0],'\n',output[1],'\n',output[2]
    
if __name__ =='__main__':
    main()