#Finding a Spliced Motif

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

def find_spliced_motif(s,t):
    """Function to find a Spliced Motif"""
    position = 0
    for symbol in t:
        print s.find(symbol,position)+1,
        position=s.find(symbol,position)+1    
    
def main():
    """Main function to find a Spliced Motif"""    
    strs = get_strs_from_input("rosalind_sseq.txt",'r')
    find_spliced_motif(strs[0],strs[1])
    
if __name__ =='__main__':
    main()
            
            