# 🔧 Adaptive Prompt Optimizer

A lightweight Python CLI tool that improves prompts for AI coding tools like GitHub Copilot and Replit.

## ✨ Features
- Accepts prompt + tool choice
- Analyzes clarity and intent
- Optimizes prompt for tool-specific behavior
- Explains why changes were made

## 📦 Requirements
- Python 3.x

## 🚀 How to Run
```bash
python main.py
```

## 🛠️ Add More Tools
- Add a new class in `optimizers/`
- Define your `optimize()` logic
- Update `get_tool_optimizer()` in `main.py`
- Add tool rules in `tool_analysis.json`

## 📄 Sample Output
```
--- Original Prompt ---
Build a to-do app

--- Optimized Prompt ---
Create a project in Replit using Python. Build a to-do app
Include file structure and code snippets.

--- Explanation ---
Added language hint for better understanding by Replit
Replit performs better with explicit file layout; added that.
```

## 📁 Folder Structure
```
main.py
optimizers/
  ├── base_optimizer.py
  ├── copilot_optimizer.py
  └── replit_optimizer.py
tool_analysis.json
utils.py
explain.py
README.md
```

---
Feel free to fork and extend!