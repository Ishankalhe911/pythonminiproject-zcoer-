# Day 14

## ✅ Topics Covered
- **Sets**
- **Dictionaries**
- **Tuples**
- **Hybrid Data Structures** (list/tuple inside dictionary, tuple inside dictionary)

---

## 🔹 Sets
- **Definition**: Unordered collection of unique elements.
- **Syntax**:  
  ```python
  seta = {"python", "java", "c++", "python"}
  print(seta)  # duplicates removed
  ```
- **Properties**:
  - No duplicates allowed.
  - Elements must be immutable (e.g., numbers, strings, tuples).
  - Cannot contain lists or other sets.
- **Example**:
  ```python
  seta = {"python", "java", "c++", "javascript", "c"}
  print(len(seta))  # counts unique elements
  ```

---

## 🔹 Dictionaries
- **Definition**: Collection of key-value pairs.
- **Syntax**:
  ```python
  dict = {
      "name": "Ishan",
      "grade": [87.5, 98.2, 54.5, 78, 67],
      "cgpa": "8.5"
  }
  ```
- **Accessing values**:
  ```python
  print(dict["grade"][2])  # 3rd marks
  ```
- **Updating values**:
  ```python
  dict["grade"][2] = 85
  print(dict)
  ```
- **Storing multiple meanings**:
  ```python
  dict = {}
  dict["table"] = ["a piece of furniture", "list of facts & figures"]
  dict["cat"] = ["a small animal"]
  print(dict)
  ```

---

## 🔹 Tuples
- **Definition**: Immutable ordered collection.
- **Syntax**:
  ```python
  tup = (1, 2, 3)
  ```
- **Special case**: Single-element tuple requires a comma.
  ```python
  tup = (9.0,)  # not just (9.0)
  ```

---

## 🔹 Hybrid Data Structures
- **List inside Dictionary**:
  ```python
  students = {
      "Ishan": [87, 92, 78],
      "Riya": [88, 95]
  }
  ```
- **Tuple inside Dictionary**:
  ```python
  dict = {
      "coordinates": (19.076, 72.877),
      "grades": (85, 90, 95)
  }
  ```

---

## 🔹 Special Problem Learned
- **Storing `9` and `9.0` uniquely in a set**:
  ```python
  seta = {9, (9.0,)}
  print(seta)  # {9, (9.0,)}
  ```
- Reason: `9` and `9.0` have the same hash → Python treats them as equal.  
  To differentiate, store `9.0` inside a tuple.

---

## 🎯 Key Takeaways
- Sets ensure uniqueness but treat `9` and `9.0` as the same.
- Dictionaries allow flexible key-value storage, including lists/tuples as values.
- Tuples are immutable and can be used inside sets/dictionaries.
- Hybrid structures (list/tuple inside dict) make data storage more powerful.
```

---

This file captures **everything you practiced today**: sets, dicts, tuples, and hybrid storage.  

👉 Do you want me to also add a **practice problems section** at the end of the file, so you can test yourself later?
