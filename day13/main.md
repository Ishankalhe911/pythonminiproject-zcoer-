# Day 13: The Hybrid Structure (Dictionary of Lists)

## 1. The Data Model

In this pattern, the **Dictionary** acts as a Category Manager, and the **List** acts as a Sequence Manager.

```python
Projects = {
    "Mobile App": [
        {"id": "BUG-01", "title": "Login crash", "status": "Open"},
        {"id": "BUG-02", "title": "Slow loading", "status": "Resolved"}
    ],
    "Website": [
        {"id": "WEB-01", "title": "Header overlapping", "status": "Open"}
    ]
}

```

---

## 2. Key Python Concepts

### The "Pointer" Variable

In Python loops, the variables you create are **references** to the actual objects in memory.

* `for project_name, bug_list in Projects.items():`
* `project_name` is a string reference.
* `bug_list` is a **reference to the entire list** sitting inside that key.



### Square Bracket Chaining `[][]`

To access data without a loop, you chain the accessors based on the data type:

1. `Projects["Mobile App"]` → Returns a **List**.
2. `Projects["Mobile App"][0]` → Returns the **first Dictionary** in that list.
3. `Projects["Mobile App"][0]["status"]` → Returns the **String** value.

---

## 3. Major Operations

### A. The Nested Traversal (The "Standard" Loop)

To touch every "Leaf" (the bug details), you must move through the hierarchy.

```python
for project, issues in Projects.items():
    print(f"Project: {project}")
    for bug in issues:  # 'bug' becomes a pointer to each dictionary in the list
        print(f"  - {bug['id']}: {bug['title']}")

```

### B. Sequence Management (List Methods)

Since the value is a list, you use list-specific methods to modify the collection:

* **Add new entry:** `Projects["Website"].append({"id": "WEB-02", ...})`
* **Remove by position:** `del Projects["Mobile App"][0]` or `Projects["Mobile App"].pop(0)`
* **Total count:** `len(Projects["Mobile App"])`

---

## 4. Why use this Hybrid?

1. **Dynamic Grouping:** The Dictionary lets you jump straight to a category ("Website") without searching.
2. **Order Preservation:** The List ensures that the sequence of items (like "First reported" to "Last reported") is never lost.
3. **Data Depth:** The inner Dictionary allows each item to have multiple attributes (ID, Title, Status) without needing a complex class structure.

---

## 5. Day 13 Practical Checklist

* [ ] **The "Status" Filter:** Loop through all projects and print only bugs where `status == "Open"`.
* [ ] **The "Specific Update":** Use `Projects["Mobile App"][1]["status"] = "Resolved"` to update a specific item.
* [ ] **The "New Project":** Add a totally new key like `"Backend"` with an empty list `[]` first, then append a bug to it.

---

