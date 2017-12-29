#Construct the Suffix Array of a String

def suffix_array(string):
    """Function to construct and return the suffix array of a string
    
    Keyword Argument:
    string -- input string
    
    Return Value:
    Returns the suffix array of the input string.
    """
    d={}
    for i in range(len(string)):
        d[i] = string[i:]
    suffix_array=""
    for key, value in sorted(d.iteritems(), key=lambda (k,v): (v,k)):
        suffix_array+= str(key)+", "
    suffix_array = suffix_array[:len(suffix_array)-2] #Removing the comma after the last number    
    return suffix_array
    
def main():
    """main function to construct the Suffix Array of a String"""
    foo = open("rosalind_ba9g.txt","r")               
    string = foo.read().strip()
    print suffix_array(string)
    foo.close()
    
if __name__ == '__main__':
    main()