#Constructing a De Bruijn Graph

import sys
from Bio.Seq import Seq

kmer_list = [];

class Node:
    """Class to hold the kmer and it's edges"""
    def __init__(self, kmer):
        """Magic object that lives in user controlled namespace"""
        self.kmer = kmer
        self.edges = set()
        
    def __str__(self):
        """Compute the nicely printable string representation of the object
        
        Return value:
        Formatted string output of the object
        """
        return "{0}".format(self.kmer)

def create_kmer_list(dna,k):
    """Create and return a list of kmers for the input dna
    
    Keyword argument:
    dna -- input dna string
    k -- length of the kmer 
    
    Return value:
    list of kmers
    """
    kmer_list = [];
    for i in range(0,len(dna)-k+1):
        kmer_list.append(dna[i:i+k])        
    return kmer_list
    
def main():
    """Main function to construct the De Bruijn Graph
    
    The function reads dna string from the file. 
    Computes the reverse complement. 
    Calls the function to create the list of kmers. 
    Constructs a De Bruijn Graph.
    """
    foo=open("rosalind_dbru.txt","r")
    dna_list=foo.read().strip().splitlines()
    dna_length=len(dna_list)
    for i in range(0,dna_length):
        dna_list.append(str(Seq(dna_list[i]).reverse_complement()))
    
    node_dict={}
    for dna in dna_list:
        last_node=None
        for kmer in create_kmer_list(dna,len(dna)-1):
            if kmer not in node_dict:
                node_dict[kmer]=Node(kmer)
            if last_node:
                last_node.edges.add(node_dict[kmer])
            last_node = node_dict[kmer]
    
    for kmer,node in sorted(node_dict.items()):
        for edge in node.edges:
            print "({0}, {1})".format(kmer,edge)

if __name__ == "__main__":
    main()    
    

        