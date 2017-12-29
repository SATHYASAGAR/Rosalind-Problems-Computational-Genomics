#Mortal Fibonacci Rabbits

def mortal_fibonacci_rabbits(n,m):
    """Returns the total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months"""
    arr = []        #arr holds the number of pairs of rabbits in each month.

    #The first two months have only one pair of rabbits.
    arr.append(1)    
    arr.append(1)

    #Calculate for the next n months
    for i in range(2,n):
        arr.append(arr[-1] + arr[-2]) if (i < m) else ((arr.append((arr[-1] + arr[-2]) - 1)) if (i == m or i == m+1) else arr.append((arr[-1] + arr[-2]) - (arr[-(m+1)])))
    return (arr[-1])

def main():
    """Main function for the mortal fibonacci rabbits problem"""
    foo=open("rosalind_fibd.txt","r")
    str=foo.read().split()
    print mortal_fibonacci_rabbits(int(str[0]),int(str[1]))
    foo.close()    
    
if __name__=='__main__':
    main()

    

