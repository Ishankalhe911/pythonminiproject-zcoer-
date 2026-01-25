# 🧩 TASK 1 — Manual Min & Max (no shortcuts)
# Implement:
# def find_min(values):
#     """
#     Returns the minimum value in the list.
#     """

# def find_max(values):
#     """
#     Returns the maximum value in the list.
#     """

# Rules:

# No min() / max()

# Handle empty list → clear error

# Single element list must work

# One-pass logic (no sorting)

# Think about:

# Why sorting is a bad idea here

# Time complexity










def find_min(values):
    """
     Returns the minimum value in the list.
    """
    
    if(len(values))==0:raise  KeyError("EMPTY LIST!!")
    crmin=values[0]
    for v in values:
        if v < crmin: 
            crmin=v
    
    return crmin



def find_max(values):
    """
    Returns the maximum value in the list.
    """
    

    #checking before loop:
    if(len(values))==0:raise KeyError("EMPTY LIST!!")
    crmax=values[0]
    for v in values:
        if v>crmax:
            crmax=v
    return crmax



print(find_min([10,20,30,40,50,]) )
print(find_max([60,10,40,50,90,47]))
