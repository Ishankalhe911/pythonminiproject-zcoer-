## 📅 Day 16 — Data Normalization & Scaling (Foundations for ML)

### 🎯 Objective

Strengthen Python fundamentals while building **ML-ready data discipline**:

* avoid data mutation
* handle edge cases explicitly
* translate math definitions into reliable code

---

## ✅ Concepts Covered

* Manual implementation of:

  * Minimum & Maximum
  * Mean Normalization
  * Min–Max Scaling
* Error handling for invalid data
* Design decisions for degenerate datasets
* Understanding why normalization matters in ML

---

## 🧩 Implemented Functions

### 1. Manual Min & Max (No Built-ins)

* One-pass traversal
* Handles empty list via `ValueError`
* Single-element lists supported naturally

**Key learning:**
Min/max does **not** require sorting → `O(n)` vs `O(n log n)`

---

### 2. Mean Normalization

**Formula:**

```
x_norm = x − μ
```

**Behavior:**

* Returns a new list
* Does NOT modify input data
* Preserves shape (N → N)

**Example:**

```
[10, 20, 30] → [-10, 0, 10]
```

**Insight:**
Normalization is a **data transformation**, not aggregation.

---

### 3. Min–Max Scaling

**Formula:**

```
x' = (x − min) / (max − min)
```

**Edge-case handling:**

* Empty list → error
* All values equal → return all zeros
* Single value → `[0]`

**Reasoning:**

* Constant features have no variance
* Returning zeros keeps pipelines stable
* Errors are for invalid data, not uninformative data

---

## 🧠 ML Insight Gained

* Models don’t understand units, only magnitudes
* Unscaled features distort optimization
* Normalization reshapes the learning space
* Data hygiene comes **before** models

---

## ⚠️ Common Pitfalls Identified & Fixed

* Returning generators instead of lists
* Placing `return` inside loops
* Silent division-by-zero errors
* Mutating input data unintentionally

---

## 🧱 Engineering Takeaways

* Correctness > shortcuts
* Explicit logic > clever syntax
* Robust behavior > “code that runs”

---

## 📌 Status

✔ Day 16 completed
✔ Code committed
✔ Ready to move to variance & standard deviation


