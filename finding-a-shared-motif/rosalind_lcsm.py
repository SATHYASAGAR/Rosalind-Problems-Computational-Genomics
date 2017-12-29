#Finding a Shared Motif

import operator

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

def get_all_substr(str):
    """Function to return all the sub strings in a given string"""
    str_len = len(str)
    return [str[i:j+1] for i in range(str_len) for j in range(i,str_len)]

def get_longest_substr(str):
    """Function to return the longest substring in a given list of strings"""
    lst=[]      #Holds all the substrings of first DNA string
    lst=get_all_substr(str[0])
    no_common_lst=[]        #Holds all the substrings of first DNA string which is not present in other DNA strings
    
    #logic to populate no_common_lst[]
    for i in lst:
        for j in str[1:]:
            if i not in j:
                no_common_lst.append(i)
                break
    
    common_lst=list(set(lst)-set(no_common_lst))        #Holds the common substrings in all the DNA strings
    
    #logic to find the substring with max length
    d={}
    for i in common_lst:
        d[i]=len(i)
    return max(d.iteritems(), key=operator.itemgetter(1))[0]
    
    
def main():
    """Main function to get the longest common substring in a given collection"""
    str = get_strs_from_input("rosalind_lcsm.txt",'r')    
    print get_longest_substr(str)
    
if __name__ =='__main__':
    main()