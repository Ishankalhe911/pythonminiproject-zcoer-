# 🏦 Day 6: Advanced Banking Application

Welcome to the Day 6 project of my Python learning journey! This is a functional command-line interface (CLI) banking system that simulates real-world account management using lists and functions.

## 📝 Project Overview
On **Day 6**, I focused on building a system that can identify a user by name, track their specific account index, and perform mathematical operations on their balance that persist throughout the session.

### 🚀 Key Features
- **User Identification:** Scans the `names` database to find the user's specific index.
- **Dynamic Transactions:** - **Withdrawal:** Deducts funds and returns the updated balance.
    - **Deposit:** Adds funds to the specific account index.
    - **Balance Check:** Instantly retrieves the current status of the account.
- **Interactive Menu:** Uses a `while True` loop to allow the user to perform multiple tasks without restarting the program.



---

## 🛠️ Technical Breakdown
The system uses three synchronized lists to manage data:
1. `names = ["A", "B", "C"]`
2. `balance = [5000, 8000, 10000]`
3. `pin = []` (Reserved for future security updates)

**Functions used:**
* `withdrawl(index, balance)`: Handles the subtraction logic.
* `deposit(index, balance)`: Handles the addition logic.
* `checkbal(index, balance)`: Handles the data retrieval.

---

## 📅 Day 6 Progress Report
- [x] Learned how to use `input()` for dynamic user choices.
- [x] Implemented list indexing to link names with balances.
- [x] Practiced `while` loops for continuous program execution.
- [x] Integrated `if-elif-else` logic for menu navigation.

---

## 🔮 Future Enhancements (Roadmap)
To make this system even more "Advanced," I plan to add:
- **Security:** Implement the `pin` check so users must enter a password to access their index.
- **Error Handling:** Add a check to see if a name exists before starting the loop to prevent `NameError`.
- **Overdraft Protection:** Prevent users from withdrawing more than their current `balance[index]`.
- **Data Persistence:** Use a `.txt` or `.json` file to save balances so they don't reset when the code stops.

---
**Author:** [Ishankalhe911](https://github.com/Ishankalhe911)  
**Project Status:** Day 6 Completed ✅
