#Compute the Probability of a Hidden Path

def extract_components(file_name):
    """extracts and returns the observations, states, and transition matrix from the input file"""    
    observations=""
    states=[]
    transition_matrix={}    
    foo=open(file_name,'r')
    components = foo.read().split("--------")
    observations=components[0].strip();
    states = components[1].strip().split();
    components[2] = components[2].strip('\n')
    transition_matrix_elements = components[2].strip('\n').replace('\n','').replace('A','').replace('B','').strip().split()
    transition_matrix['AA']=float(transition_matrix_elements[0])
    transition_matrix['AB']=float(transition_matrix_elements[1])
    transition_matrix['BA']=float(transition_matrix_elements[2])
    transition_matrix['BB']=float(transition_matrix_elements[3])   
    
    return observations,states,transition_matrix
    
def generate_kmer(string,k):
    """This function returns the kmer composition of a string"""
    composition = [];
    for i in range(0,len(string)-k+1):
        composition.insert(0,string[i:i+k])
    return composition

def main():
    """main function to compute the Probability of a Hidden Path"""
    observations,states,transition_matrix = extract_components("rosalind_ba10a.txt")
    two_mer_composition=generate_kmer(observations,2)
    probability = 0.5 #Initial probability 
    for value in two_mer_composition:
        probability = probability * transition_matrix[value]    
    print probability             
    
if __name__ =='__main__':
    main()