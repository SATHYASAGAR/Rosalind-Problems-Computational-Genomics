#Mendel's First Law

def get_values_from_input(file_name,mode):
    """Function to get the values of k, m and n from a file.
    
    Keyword Argument:
    file_name -- name of the file
    mode -- mode in which the file needs to be opened
    
    Return Value:
    Returns the values.
    """
    foo = open(file_name,mode)                   
    values = foo.read().split()            
    return values

def main():
    """main function to find the probability that two randomly selected mating organisms will produce an individual possessing a dominant allele"""
    values = get_values_from_input("rosalind_iprb.txt",'r') 
    
    k=int(values[0])
    m=int(values[1])
    n=int(values[2])

    sum_of_k_m_n=float(k+m+n);

    kk_km_kn = (k/sum_of_k_m_n * (k-1)/(sum_of_k_m_n-1)) + (k/sum_of_k_m_n * m/(sum_of_k_m_n-1)) + (k/sum_of_k_m_n * n/(sum_of_k_m_n-1))
    mm_mk_nn = (m/sum_of_k_m_n * (m-1)/(sum_of_k_m_n-1) * 3/4) + (m/sum_of_k_m_n * k/(sum_of_k_m_n-1)) + (m/sum_of_k_m_n * n/(sum_of_k_m_n-1) * 1/2)
    nn_nk_nm = (n/sum_of_k_m_n * k/(sum_of_k_m_n-1)) + (n/sum_of_k_m_n * m/(sum_of_k_m_n-1)* 1/2)

    probability = kk_km_kn + mm_mk_nn + nn_nk_nm

    print round(probability,5)
    
if __name__ =='__main__':
    main()
