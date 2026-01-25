#🧩 TASK 1 — Mean (from scratch)
#Handle:
#empty list → raise a clear error
#list with one element
#Do manual summation
#Return a float


def mean(values):

    """
    Takes a list of numbers.
    Returns the arithmetic mean.
    """
    
    
    
    total=0
    if(len(values))==0:
        raise ValueError("Cannot compute mean of empty list")

    for i in range(len(values)):
        
        total=total+(values[i])
    
    mean=total/len(values)
    

        return mean
 

def variance(values):
    """
    Returns variance of the list.
    """




    meninv= mean(values)
    summation=0
    for i in range(len(values)):
        summation=summation+((values[i]-meninv)**2)
    

    variance=summation/len(values)
    return variance

variance([100])

     


    
