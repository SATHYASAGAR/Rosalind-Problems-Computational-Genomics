#Conditions and Loops

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

def sum_of_all_odd_integers(a,b):
    """Function to return the sum of all odd integers from a to b, inclusive"""
    sum=0
    for i in range(a,b+1):
        if(i%2==1):
            sum+=i
    return sum
    
def main():
    """Main function to print the sum of all odd integers between the given range"""
    foo=open("rosalind_ini4.txt",'r')
    numbers = foo.read().split()
    print sum_of_all_odd_integers(int(numbers[0]),int(numbers[1]))
    
if __name__ =='__main__':
    main()