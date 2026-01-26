##DAY 17

---

# 📊 Statistical Foundations & Z-Score Normalization

This project implements a custom statistical library to calculate the variance, standard deviation, and Z-score normalization of a dataset without using external libraries like `numpy` or `scipy`.

## 🛠️ Implementation

### 1. Central Tendency & Dispersion

The foundation requires calculating the mean and how much the data "spreads" (variance).

**Mathematical Formulas:**

* **Mean ():=sum of all terms /totalno of terms** 
* **Population Variance (): summation from  all 0 to N of(v-mean)^2/totalno of values** 
* **Standard Deviation (): sqrt of Variance or 0.5 ** **variance**** 

```python
def mean(values):
    """Returns the arithmetic mean of a list."""
    if len(values) == 0:
        raise ValueError("Cannot compute mean of empty list")
    
    total = sum(values)
    return total / len(values)

def variance(values):
    """Returns the population variance."""
    if len(values) == 0:
        raise ValueError("Empty list, variance can't be calculated")
    
    mn = mean(values)
    sum_sq_diff = sum((v - mn)**2 for v in values)
    
    return sum_sq_diff / len(values)

def std_deviation(values):
    """Returns the standard deviation."""
    return variance(values)**0.5

```

### 2. Z-Score Normalization

This function transforms data to have a **mean of 0** and a **standard deviation of 1**.

**Formula: new element of z score normalization list= v-mean/std_dev** 

```python
def zscorenorm(values):
    """Performs Z-score normalization on a list of values."""
    zeroscorelst = []
    mn = mean(values)
    vstd = std_deviation(values)
    
    for v in values:
        newel = (v - mn) / vstd
        zeroscorelst.append(newel)

    return zeroscorelst

```

---

## 🧠 Conceptual Q&A

> **Q1: Why do we square ?** > **A:** If we didn't square the differences, the positive and negative distances from the mean would cancel each other out (summing to zero). Squaring ensures all distances are positive and gives more weight to outliers.

> **Q2: Why divide by ?** > **A:** We divide by  to find the **average** squared deviation. This gives us a single representative value for the spread of the entire population regardless of the sample size.

> **Q3: Why is variance never negative?** > **A:** Since variance is the average of squared numbers, and the square of any real number is always , the result is mathematically impossible to be negative. It represents "magnitude of spread," which can't be less than nothing.

---

