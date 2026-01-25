

# 🧩 TASK 3 — Min–Max Scaling
# Implement:
# def min_max_scale(values):
#     """
#     Scales values to range [0, 1].
#     """

# Formula:
# 𝑥'=𝑥 −𝑚𝑖𝑛 /𝑚𝑎𝑥−𝑚𝑖𝑛x


# Rules (non-negotiable)

# Use your own find_min() and find_max()

# ❌ Do NOT modify input list

# ✅ Return a new list

# Handle empty list → clear error

# Handle case where all values are equal

# Decide: error or all zeros (justify by behavior)


def find_min(values):
    """
     Returns the minimum value in the list.
    """
    
    if(len(values))==0:raise  ValueError("EMPTY LIST!!")
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
    if(len(values))==0:raise ValueError("EMPTY LIST!!")
    crmax=values[0]
    for v in values:
        if v>crmax:
            crmax=v
    return crmax

def min_max_scale(values):
     """
     Scales values to range [0, 1].
    """
     minim=find_min(values)
     maxim=find_max(values)
     minmaxlst=[]
     

     if minim==maxim  :
     #single element in the list 
      for i in range(len(values)):
         
         minmaxlst.append(0)
      return minmaxlst
         

     
         
     else:
      for v in values :
         newel=(v-minim)/(maxim-minim)
         minmaxlst.append(newel)
      return minmaxlst


print(min_max_scale([10,10,10,10]))
         
     








