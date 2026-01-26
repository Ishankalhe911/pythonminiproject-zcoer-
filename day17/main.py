# 🧩 TASK 1 — Variance (Population Variance)
# Mathematical definition (lock this in):
# 𝜎
# 2
# =
# 1
# 𝑁
# ∑
# (
# 𝑥
# −
# 𝜇
# )
# 2
# σ
# 2
# =
# N
# 1
# 	​

# ∑(x−μ)
# 2
# Implement:
# def variance(values):
#     """
#     Returns the population variance of the list.
#     """

# Rules:

# Must use your own mean()

# One pass to compute squared deviations

# Empty list → error

# Single value → variance = 0

# Return a float

# Do NOT print — return

# ⚠️ No extra conditions unless mathematically justified

# 🧠 Think BEFORE coding

# Answer these to yourself (don’t Google):

# Why do we square (x − mean)?

# Why divide by N?

# Why is variance never negative?

# If you can’t answer, pause.
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
     Returns the population variance of the list.
    """
    if (len(values)==0):
        raise ValueError("Empty list ,variance can't be calculated")
    mn=mean(values)
    summat=0
    #variance=sum of all 0 to n [(x-mean)^2]/no of the total values in the list .......so add all(all means 0 to n) (v-mean)^2 and then /totalval
    #one thing could be remembered if there is summation there has to be +=
    for v in values:
        summat=summat+((v-mn)**2)
    variance=(summat/len(values))
    return variance




#std dev
def std_deviation(values):
    var=variance(values)
    stddev=var**0.5
    
    return stddev
    

print(std_deviation([10,20,30]))










#q&a answers
#a1) we square (x-mean) because here we are in the variance function and variance of  data can't be negetive it can be either zero or a positive integer hence we need to square the difference

#a2) so see here we did the (x-mean) so we got the variance of that specific value or data from the avg of the dataset hence to find a single avg of all the variane at the last we do divide by N hence we get final avg variance of the dataset

#a3)as variance is a quanity which tells us by varyness of the dataset and which surely logically can't be negetive at all and for that also we do the square and from there we can get the standard deviation of the whole dataset 
