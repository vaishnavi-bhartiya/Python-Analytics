# 🧮 Python Calculator

This project is a simple **command-line calculator** built in Python.  
It supports basic arithmetic operations and keeps a history of all calculations performed during a session.

---

## ✨ Features
- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/), with division-by-zero handling
- Modulus (%)
- Exponentiation (**)
- Calculation history view
- Exit option to end the program

---

## 📂 Project Structure
Calculator/
├── calculator.py   # Contains the calculator function logic
├── main.py         # Interactive program with history tracking
└── README.md       # Project documentation

---

## ▶️ How to Run
1. Clone this repository or download the files.
   ```bash
   git clone https://github.com/vaishnavi-bhartiya/Python-Analytics.git
   cd Python-Analytics/Calculator
   ```
   
2. Run the program.
   ```bash
   python main.py
   ```
   
3. Follow the prompts:
- Enter an operation (+, -, *, /, %, **)
- Enter two numbers
- View the result
- Type ```history``` to see past calculations
- Type ```exit``` to quit
  
---

## 📝 Example Run
```bash
Enter operation (+,-,/,*,%,**) or type 'exit'/'history': +
Enter 1st number: 10
Enter 2nd number: 5
result of 10.0 + 5.0 = 15.0

Enter operation (+,-,/,*,%,**) or type 'exit'/'history': history
Calculation History
1. result of 10.0 + 5.0 = 15.0
```
---

## 🎯 Purpose
This project demonstrates:
- Python basics (functions, loops, conditionals)
- Error handling
- User interaction via command-line
- Clean project structure with modular code

---

## 🚀 Future Enhancements
- Add unit tests.
- Build a GUI version using Tkinter.
- Extend with advanced mathematical functions.
