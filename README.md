# 🚀 DecodeLabs Python Programming Projects

> **Industrial Training Kit — Batch 2026 | Powered by DecodeLabs**

A collection of 4 Python backend projects completed as part of the DecodeLabs Industrial Training Program. Each project builds on core programming concepts — from data management and financial logic to security tools and decision engines.

---

## 📁 Repository Structure

```
decodelabs_tasks/
├── todo.py
├── expense_tracker.py
├── password_generator.py
├── quiz.py
└── README.md     ← You are here
```

---

## 📌 Projects Overview

### Project 1 — 📝 To-Do List
**Focus: Data Management & Lists**

A command-line task manager where users can add and view tasks interactively.

| Detail | Info |
|--------|------|
| Key Skill | Lists, `append()`, `enumerate()`, `while` loop |
| Concepts | Dynamic arrays, IPO model, volatile memory |
| Run | `python todo.py` |

**Quick Demo:**
```
Enter a task (or 'quit' to exit): Buy Milk
Your Tasks:
1. Buy Milk
```

---

### Project 2 — 💰 Expense Tracker
**Focus: Data Accumulation & Math Operations**

A real-time expense tracker with running totals, input validation, and formatted financial output.

| Detail | Info |
|--------|------|
| Key Skill | Accumulators (`total += expense`), `try/except`, `while` loop |
| Concepts | State management, IPO model, sentinel values |
| Run | `python expense_tracker.py` |

**Quick Demo:**
```
Enter expense amount (or 'quit' to exit): 25.50
  ✅ Added: $25.50
  📊 Running Total: $25.50
```

---

### Project 3 — 🔐 Random Password Generator
**Focus: Library Integration & Security**

A cryptographically secure password generator using Python's `secrets` module with entropy scoring.

| Detail | Info |
|--------|------|
| Key Skill | `import secrets`, `import string`, `.join()` |
| Concepts | Cryptographic randomness, entropy (`E = L × log₂R`), NIST 2024 standards |
| Run | `python password_generator.py` |

**Quick Demo:**
```
Enter desired password length (minimum 8): 16
Generated Password : aB3$kL9!mN2@pQ7&
Entropy Score      : 104.86 bits
Strength           : Very Strong
```

---

### Project 4 —  General Knowledge Quiz
**Focus: Control Flow & Decision Engine**

An interactive quiz program with if/else logic, input sanitization, and score tracking.

| Detail | Info |
|--------|------|
| Key Skill | `if/elif/else`, `for` loop, `.strip()`, `.casefold()` |
| Concepts | Control flow, input sanitization, accumulator pattern, IPOS architecture |
| Run | `python quiz.py` |

**Quick Demo:**
```
Question 1: What is the capital of France?
Your answer: paris
Correct! ✓

Quiz Complete! Your Score: 3/3
Excellent! Perfect Score! 
```

---

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Libraries:** `secrets`, `string`, `math` (standard library only)
- **No external dependencies required**

---

## ▶️ How to Run Any Project

```bash
# Clone the repository
git clone https://github.com/your_username/decodelabs_tasks.git

# Navigate to a project folder
cd decodelabs_tasks/project_1_todo_list

# Run the script
python todo.py
```

---

## 🧠 Concepts Covered Across All Projects

| Concept | Project |
|---------|---------|
| Lists & Dynamic Arrays | Project 1 |
| While Loops & Sentinel Values | Project 1, 2 |
| Math Operations & Accumulators | Project 2 |
| try/except Error Handling | Project 2, 3 |
| Module Imports & Standard Library | Project 3 |
| Cryptographic Security (`secrets`) | Project 3 |
| if/elif/else Control Flow | Project 4 |
| Input Sanitization | Project 4 |
| For Loops & Dictionaries | Project 4 |
| IPO / IPOS Architecture | All Projects |

---

## 👨‍💻 Author

**Intern — DecodeLabs Industrial Training Program**
Batch: 2026

---

*Built with ❤️ at DecodeLabs — Where Code Meets Engineering.*
