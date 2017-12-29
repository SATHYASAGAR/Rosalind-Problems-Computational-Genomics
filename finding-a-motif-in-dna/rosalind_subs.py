#Finding a Motif in DNA

"""
Given: Two DNA strings s and t (each of length at most 1 kbp).
Return: All locations of t as a substring of s.
"""

def find_motif_in_dna(s,t):
    """Function to find Motif in DNA.
    
    Keyword Argument:
    s -- first DNA string
    t -- second DNA string
    
    Return Value:
    Returns all the location of the substring in the main string.
    """
    pos=[]      #pos holds the location of the substring in the main string
    len_t=len(t)
    for i in range(len(s)-len_t+1):
        if s[i:i+len_t]==t:
            pos.append(i+1)
    return pos
    

def main():
    """Main function to calculate the hamming distance.

    The function reads two dna string from the file. 
    Computes and prints all location of the substring in the main string.
    """
    foo=open("rosalind_subs.txt","r")
    strt=foo.read().splitlines()
    motif_array = find_motif_in_dna(strt[0],strt[1])
    for i in motif_array:
        print i,
    foo.close()
    
if __name__ =='__main__':
    main()