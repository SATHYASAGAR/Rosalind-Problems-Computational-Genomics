#Counting Point Mutations

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
    """Main function to calculate the hamming distance
    
    The function reads two dna string from the file. 
    Computes and prints the hamming distance.
    """
    foo=open('rosalind_hamm.txt','r')
    lst = foo.read().strip().split()  
    print hamming_distance(lst[0],lst[1])
    foo.close()
    
if __name__ =='__main__':
    main()