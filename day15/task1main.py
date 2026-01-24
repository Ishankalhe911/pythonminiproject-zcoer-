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

    for i in range(len(values)):
        
        total=total+(values[i])
    if(len(values))==0:
        raise ValueError("Cannot compute mean of empty list")
    elif total==0:
        mean=0
        return mean
    elif len(values) == 1: 
        mean=float(values[0])
        return mean

        
    elif total==1:
        mean=1
        return mean
    else:
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
    print(variance)

variance([100])

     


    
