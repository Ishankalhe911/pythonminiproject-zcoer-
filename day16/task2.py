# 📅 DAY 2 — TASK 2: Mean Normalization (now)
# Goal

# Learn data transformation without mutation — a core ML habit.

# 🧩 TASK 2 — Mean Normalization
# Implement:
# def mean_normalize(values):
#     """
#     Returns a new list where each value is mean-normalized.
#     """

# Formula
# 𝑥
# 𝑛
# 𝑜
# 𝑟
# 𝑚
# =
# 𝑥
# −
# 𝜇
# x
# norm
# 	​

# =x−μ
# Rules (read carefully)

# Must use your own mean() from Day 1

# ❌ Do NOT modify the original list

# ✅ Return a new list

# Handle empty list → clear error

# No NumPy, no shortcuts

# Why this task matters

# This is where many students accidentally:

# mutate data

# cause silent bugs

# break pipelines

# If you mutate input data in ML, you introduce non-reproducible bugs.
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
 
def mean_normalize(values):
     """
     Returns a new list where each value is mean-normalized.
     """
     norm_list=[]
     meanres=mean(values)

     for v in values:
         #normalization=current value-mean
         normval=v-meanres
         
         norm_list.append(normval)
     
     return norm_list


print(mean_normalize([10,20,30]))