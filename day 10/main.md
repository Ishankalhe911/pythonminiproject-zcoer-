# Day 10: Advanced List Logic & Iteration

## 📝 Overview

Today’s focus was on manual data manipulation. Instead of relying on built-in Python shortcuts, we implemented logic from scratch to understand how data is traversed, compared, and tracked using loops.

---

## 🛠️ Tasks Completed

### 1. List Palindrome Checker

**Goal:** Determine if a list reads the same forward and backward.

* **Method:** Two-Pointer Approach.
* **Logic:** * Set a pointer at the `start` (index 0) and `end` (last index).
* Compare elements at both pointers.
* If any pair doesn't match, set `is_palindrome` to `False` and `break` immediately to save processing time.


* **Key Concept:** Efficiency through early exit.

### 2. Frequency Checker (Manual Logic)

**Goal:** Count how many times each unique element appears in a list without using Python Dictionaries or the `Counter` module.

* **Method:** Nested Loops with a "Seen" List.
* **Logic:**
* **Outer Loop:** Iterates through every element in the input data.
* **Skip Logic:** A secondary list (`numb`) keeps track of elements already counted. If an element is found in `numb`, it is skipped.
* **Counting Loop:** If it's a new element, a third loop scans the entire list to increment the `freq` counter.


* **Key Concept:** State management and preventing duplicate output.

---

## ⚠️ Lessons Learned (Bug Fixes)

| Error Encountered | Cause | Solution |
| --- | --- | --- |
| **AttributeError** | Trying to `.append()` to an integer variable. | Use `.append()` only on List objects. |
| **Syntax Error** | Using `list(k)` to access an index. | Use square brackets for indexing: `list[k]`. |
| **Logic Error** | Using `freq =+ 1`. | Use `+= 1` to increment. `=+` just sets the value to positive 1. |
| **Indentation** | Printing frequency inside the wrong loop. | Indent the `print` inside the "New Element" check (`if skipcnt == 0`). |
| **LOOP ISSUES**||
| **LOGIC ISSUES WRT LOOP AND SILLY MISTAKES**|

---

## 🚀 Looking Ahead: Day 11

**Focus:** Data Filtering, Transformation, and Comparison Logic.

* **Task:** Separating Odds/Evens, performing math transformations (Squaring/Cubing), and finding Max/Min values manually.

---

