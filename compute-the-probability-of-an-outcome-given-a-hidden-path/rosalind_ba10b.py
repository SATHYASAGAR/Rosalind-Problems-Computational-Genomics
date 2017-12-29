#Compute the Probability of an Outcome Given a Hidden Path

def extract_components(file_name):
    """This function extracts and returns the observations, states, and transition matrix from the input file"""    
    states=[]
    emission_matrix={}    
    foo=open(file_name,'r')
    components = foo.read().split("--------")
    
    string=components[0].strip();
    transition = components[1].strip().split();
    alphabet = components[2].strip()
    states = components[3].strip().split();
    
    emission_matrix_elements = components[4].strip('\n').replace('\n','')    
    for character in ['A','B','x','y','z']:
        if character in emission_matrix_elements:
            emission_matrix_elements=emission_matrix_elements.replace(character,'')
    
    emission_matrix_elements = emission_matrix_elements.strip().split()
    
    emission_matrix['Ax']=float(emission_matrix_elements[0])
    emission_matrix['Ay']=float(emission_matrix_elements[1])
    emission_matrix['Az']=float(emission_matrix_elements[2])
    emission_matrix['Bx']=float(emission_matrix_elements[3])   
    emission_matrix['By']=float(emission_matrix_elements[4])
    emission_matrix['Bz']=float(emission_matrix_elements[5])
    
    return string,transition,alphabet,states,emission_matrix
    
def generate_compositions(string1,string2):
    """This function returns the compositions given two strings"""
    composition = [];
    for i in range(0,len(string1)):
        composition.insert(0,string2[i]+string1[i])
    return composition

def main():
    """Main function to compute the Probability of an Outcome Given a Hidden Path"""
    string,transition,alphabet,states,emission_matrix = extract_components("rosalind_ba10b.txt")
    composition=generate_compositions(string,alphabet)
    probability = 1.0
    for value in composition:
        probability = probability * emission_matrix[value]    
    print probability             
    
if __name__ =='__main__':
    main()