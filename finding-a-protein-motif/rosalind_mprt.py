#Finding a Protein Motif

import urllib
import re

def list_motif_loc(id,str1,regexp):
    """This function lists the access ID followed by a list of locations in the protein string where the motif can be found"""
    lst=[] 
    for i in range(len(str1)-4):
        m = re.search(regexp,str1[i:i+4])
        if m is not None:
            lst.append(m.group(0))
    if len(lst)>0:
        print id
        for i in lst:
            print str1.find(i)+1,
        print 

def main():
    """Main function for finding a protein motif"""
    regexp='N[^P][ST][^P]'
    foo=open("rosalind_mprt.txt","r")
    input=foo.read().splitlines()
    for id in input:
        url="http://www.uniprot.org/uniprot/"+id+".fasta"
        filehandle = urllib.urlopen(url)
        str=filehandle.read().splitlines()
        str1=''
        for i in str[1:]:
            str1+=i

        list_motif_loc(id,str1,regexp)
        
    foo.close()
    
if __name__ =='__main__':
    main()