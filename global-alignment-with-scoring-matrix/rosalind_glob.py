#Global Alignment with Scoring Matrix

from numpy import zeros

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
    """Main function to print the maximum alignment score between two strings s and t"""
    protein_strings = get_strs_from_input("rosalind_glob.txt",'r')   
    s=protein_strings[0]
    t=protein_strings[1]    
    BLOSUM62 = [[4,0,-2,-1,-2,0,-2,-1,-1,-1,-1,-2,-1,-1,-1,1,0,0,-3,-2],[0,9,-3,-4,-2,-3,-3,-1,-3,-1,-1,-3,-3,-3,-3,-1,-1,-1,-2,-2],[-2,-3,6,2,-3,-1,-1,-3,-1,-4,-3,1,-1,0,-2,0,-1,-3,-4,-3],[-1,-4,2,5,-3,-2,0,-3,1,-3,-2,0,-1,2,0,0,-1,-2,-3,-2],[-2,-2,-3,-3,6,-3,-1,0,-3,0,0,-3,-4,-3,-3,-2,-2,-1,1,3],[0,-3,-1,-2,-3,6,-2,-4,-2,-4,-3,0,-2,-2,-2,0,-2,-3,-2,-3],[-2,-3,-1,0,-1,-2,8,-3,-1,-3,-2,1,-2,0,0,-1,-2,-3,-2,2],[-1,-1,-3,-3,0,-4,-3,4,-3,2,1,-3,-3,-3,-3,-2,-1,3,-3,-1],[-1,-3,-1,1,-3,-2,-1,-3,5,-2,-1,0,-1,1,2,0,-1,-2,-3,-2],[-1,-1,-4,-3,0,-4,-3,2,-2,4,2,-3,-3,-2,-2,-2,-1,1,-2,-1],[-1,-1,-3,-2,0,-3,-2,1,-1,2,5,-2,-2,0,-1,-1,-1,1,-1,-1],[-2,-3,1,0,-3,0,1,-3,0,-3,-2,6,-2,0,0,1,0,-3,-4,-2],[-1,-3,-1,-1,-4,-2,-2,-3,-1,-3,-2,-2,7,-1,-2,-1,-1,-2,-4,-3],[-1,-3,0,2,-3,-2,0,-3,1,-2,0,0,-1,5,1,0,-1,-2,-2,-1],[-1,-3,-2,0,-3,-2,0,-3,2,-2,-1,0,-2,1,5,-1,-1,-3,-3,-2],[1,-1,0,0,-2,0,-1,-2,0,-2,-1,1,-1,0,-1,4,1,-2,-3,-2],[0,-1,-1,-1,-2,-2,-2,-1,-1,-1,-1,0,-1,-1,-1,1,5,0,-2,-2],[0,-1,-3,-2,-1,-3,-3,3,-2,1,1,-3,-2,-2,-3,-2,0,4,-3,-1],[-3,-2,-4,-3,1,-2,-2,-3,-3,-2,-1,-4,-4,-2,-3,-3,-2,-3,11,2],[-2,-2,-3,-2,3,-3,2,-1,-2,-1,-1,-2,-3,-1,-2,-2,-2,-1,2,7]];
    linear_gap_penalty = 5
    character_index_dict ={'A':0,'C':1,'D':2,'E':3,'F':4,'G':5,'H':6,'I':7,'K':8,'L':9,'M':10,'N':11,'P':12,'Q':13,'R':14,'S':15,'T':16,'V':17,'W':18,'Y':19}
    global_alignment_matrix=zeros((len(s)+1,len(t)+1), dtype=int)
    for i in xrange(0,len(s)+1):
        global_alignment_matrix[i][0]=0
    for j in xrange(1,len(t)+1):
        global_alignment_matrix[0][j]=0
    for i in xrange(1,len(s)+1):
        global_alignment_matrix[i][0]=global_alignment_matrix[i-1][0]-linear_gap_penalty
    for j in xrange(1,len(t)+1):
        global_alignment_matrix[0][j]=global_alignment_matrix[0][j-1]-linear_gap_penalty
    for i in xrange(1,len(s)+1):
        for j in xrange(1,len(t)+1):
            if(s[i-1] not in character_index_dict.keys()):
                first_index=-1
            else:
                first_index=character_index_dict[s[i-1]]
            if(t[j-1] not in character_index_dict.keys()):
                second_index=-1
            else:
                second_index=character_index_dict[t[j-1]]    
            global_alignment_matrix[i][j]= max(max(global_alignment_matrix[i-1][j]-linear_gap_penalty,global_alignment_matrix[i][j-1]-linear_gap_penalty),global_alignment_matrix[i-1][j-1]+BLOSUM62[first_index][second_index])
    print global_alignment_matrix[len(s)][len(t)]
    
if __name__=="__main__":
    main()   