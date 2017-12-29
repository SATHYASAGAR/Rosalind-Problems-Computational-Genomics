#Open Reading Frames

def open_reading_frames(dna):
    """Returns reading frames for each dna sequence
    
    Keyword argument:
    dna -- dna input string
    
    Return value:
    reading frames for the input dna sequence
    """
    rc=reverse_complement(dna)
    return [dna, dna[1:],dna[2:],rc,rc[1:],rc[2:]]

def translate(rna):
    """Translate rna into a protein
    
    Keyword argument:
    rna -- rna input string
    
    Return value:
    translated protein string
    """
    codon_table = {'UUU':'F',	'UUC':'F',	'UUA':'L',	'UUG':'L',	'UCU':'S',	'UCC':'S',	'UCA':'S',	'UCG':'S',	'UAU':'Y',	'UAC':'Y',	'UAA':'Stop',	'UAG':'Stop',	'UGU':'C',	'UGC':'C',	'UGA':'Stop',	'UGG':'W',	'CUU':'L',	'CUC':'L',	'CUA':'L',	'CUG':'L',	'CCU':'P',	'CCC':'P',	'CCA':'P',	'CCG':'P',	'CAU':'H',	'CAC':'H',	'CAA':'Q',	'CAG':'Q',	'CGU':'R',	'CGC':'R',	'CGA':'R',	'CGG':'R',	'AUU':'I',	'AUC':'I',	'AUA':'I',	'AUG':'M',	'ACU':'T',	'ACC':'T',	'ACA':'T',	'ACG':'T',	'AAU':'N',	'AAC':'N',	'AAA':'K',	'AAG':'K',	'AGU':'S',	'AGC':'S',	'AGA':'R',	'AGG':'R',	'GUU':'V',	'GUC':'V',	'GUA':'V',	'GUG':'V',	'GCU':'A',	'GCC':'A',	'GCA':'A',	'GCG':'A',	'GAU':'D',	'GAC':'D',	'GAA':'E',	'GAG':'E',	'GGU':'G',	'GGC':'G',	'GGA':'G',	'GGG':'G'}
    protein=''
    i=0
    while i<len(rna):
        if len(rna[i:i+3])!=3:
            break;
        print rna[i:i+3]
        if codon_table[rna[i:i+3]] == 'Stop':
            protein+='*'
        else:
            protein+= (codon_table[rna[i:i+3]])
        i+=3    	
    return protein
    
def transcribe(dna):
    """Transcribe dna into rna
    
    Keyword argument:
    dna -- dna input string
    
    Return value:
    transcribed rna string
    """
    return dna.replace('T','U')
    
def reverse_complement(string):
    """Reverse complement of a string
    
    Keyword argument:
    string -- input string
    
    Return value:
    reverse complement of the imput string
    """
    rc=''
    for i in string:
        if i=='A':
            rc+='T'            
        elif i=='T':
            rc+='A'            
        elif i=='C':
            rc+='G'            
        elif i=='G':
            rc+='C'                
        else:
            rc+=i
    rc=rc[::-1]
    return rc
    
def main():
    foo = open("rosalind_orf.txt",'r')
    strt = foo.read()
    seq=strt.strip().split('>')
    str = []            
    for s in seq:       #Concatinate all the multiline strings
        if(s!=""):
            all_str=s.split()
            str1=all_str[0]
            str2=''.join(all_str[1:])
            str.append(str2)
    dna = str[0]
    distinct_candidate_proteins={}
    frames = open_reading_frames(dna)
    for frame in frames:
        print "DNA: "+frame
        rna = transcribe(frame)
        print "RNA: "+rna
        protein = translate(rna)
        print "PROTEIN: "+ protein
        for index, letter in enumerate(protein):
            if letter=='M':
                for innerIndex, innerLetter in enumerate(protein[index:]):
                    if innerLetter=='*':
                        distinct_candidate_proteins[protein[index:index+innerIndex]]=0
                        break
    for candidate_protein in distinct_candidate_proteins.keys():
        print candidate_protein
        
if __name__ == "__main__":
    main()  
    
