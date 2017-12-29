#Error Correction in Reads

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

def reverse_complement(str):
    """function to find the reverse complement of a given string    
    
    Keyword Argument:
    str -- string whose reverse_complement needs to be returned
    
    Return Value:
    Returns the reverse_complement of the input string.
    """
    reverse_complement=''
    for i in str:
        if i=='A':
            reverse_complement+='T'            
        elif i=='T':
            reverse_complement+='A'            
        elif i=='C':
            reverse_complement+='G'            
        elif i=='G':
            reverse_complement+='C'                
        else:
            reverse_complement+=i
    reverse_complement=reverse_complement[::-1]
    return reverse_complement

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
    reads = get_strs_from_input("rosalind_corr.txt",'r');
    
    read_dict={} #contains reads as keys and occurance count as values
    for read in reads:
        read_dict[read]=read_dict.get(read,0)+1
    
    #Below loop increments occurance count in read_dict if it's reverse count is present in the list of reads    
    for key,value in read_dict.iteritems():
        if(value==1):
            if reverse_complement(key) in list(read_dict.keys()):
                read_dict[key]=value+1;
    print read_dict
    incorrect_reads={} #Contains the reads which occur only once and has hamming_distance of 1 with a correct read or reverse_complement of correct read
    for key,value in read_dict.iteritems():
        if(value==1):
            for key2,value2 in read_dict.iteritems():
                if(value2>1 and key!=key2 and (hamming_distance(key,key2)==1)):
                    incorrect_reads[key]=key2   
                    
    for key,value in read_dict.iteritems():
        if(value==1):
            for key2,value2 in read_dict.iteritems():
                if((key not in incorrect_reads) and value2>1 and key!=key2 and (hamming_distance(key,reverse_complement(key2))==1)):
                    incorrect_reads[key]=reverse_complement(key2)  
    
    #prints in the rosalind required format
    for key,value in incorrect_reads.iteritems():
        print key+"->"+value
    
if __name__=='__main__':
    main()
    
    