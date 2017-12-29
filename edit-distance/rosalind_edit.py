#Edit Distance

from numpy import zeros

def find_edit_distance(string1,string2):
    """Function to find the edit distance between two protein strings.
    
    Keyword Argument:
    string1 -- first protein string
    string2 -- second protein string
    
    Return Value:
    Returns the edit distance between two strings.
    """
    M=zeros((len(string1)+1,len(string2)+1), dtype=int)
    for i in xrange(1,len(string1)+1):
        M[i][0]=i
    for j in xrange(1,len(string2)+1):
        M[0][j]=j
    for i in xrange(1,len(string1)+1):
        for j in xrange(1,len(string2)+1):
            if(string1[i-1]!=string2[j-1]):
                M[i][j] = min(M[i - 1][j] + 1, M[i][j - 1] + 1, M[i - 1][j - 1] + 1)
            else:
                M[i][j] = M[i - 1][j - 1]
    return M[len(string1)][len(string2)]

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
    
def main():
    """main function to get the edit distance"""
    strs=get_strs_from_input("rosalind_edit.txt",'r')
    print find_edit_distance(strs[0],strs[1])
        
if __name__ =='__main__':
    main()