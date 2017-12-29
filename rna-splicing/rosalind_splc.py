#RNA Splicing

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
    """main function to perform RNA splicing"""
    strs = get_strs_from_input("rosalind_splc.txt",'r') 
    for i in range(1,len(strs)):
        strs[0]=strs[0].replace(strs[i],'')
    strs[0]=strs[0].replace('T','U')
    s=strs[0]
    codon_table = {'UUU':'F',	'UUC':'F',	'UUA':'L',	'UUG':'L',	'UCU':'S',	'UCC':'S',	'UCA':'S',	'UCG':'S',	'UAU':'Y',	'UAC':'Y',	'UAA':'Stop',	'UAG':'Stop',	'UGU':'C',	'UGC':'C',	'UGA':'Stop',	'UGG':'W',	'CUU':'L',	'CUC':'L',	'CUA':'L',	'CUG':'L',	'CCU':'P',	'CCC':'P',	'CCA':'P',	'CCG':'P',	'CAU':'H',	'CAC':'H',	'CAA':'Q',	'CAG':'Q',	'CGU':'R',	'CGC':'R',	'CGA':'R',	'CGG':'R',	'AUU':'I',	'AUC':'I',	'AUA':'I',	'AUG':'M',	'ACU':'T',	'ACC':'T',	'ACA':'T',	'ACG':'T',	'AAU':'N',	'AAC':'N',	'AAA':'K',	'AAG':'K',	'AGU':'S',	'AGC':'S',	'AGA':'R',	'AGG':'R',	'GUU':'V',	'GUC':'V',	'GUA':'V',	'GUG':'V',	'GCU':'A',	'GCC':'A',	'GCA':'A',	'GCG':'A',	'GAU':'D',	'GAC':'D',	'GAA':'E',	'GAG':'E',	'GGU':'G',	'GGC':'G',	'GGA':'G',	'GGG':'G'}
    protein_string=''
    i=0
    while i<=len(s):
        if codon_table[s[i:i+3]] == 'Stop':
            break
        protein_string+= (codon_table[s[i:i+3]])
        i+=3	
    print protein_string    
    
if __name__ =='__main__':
    main()