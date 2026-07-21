# 🔐 Password Strength Checker (Python OOP)

A console-based Password Strength Checker built using Python and Object-Oriented Programming (OOP). The application evaluates the strength of a password based on commonly accepted security rules.

## Features

- 🔑 Checks password length
- 🔠 Detects uppercase letters
- 🔡 Detects lowercase letters
- 🔢 Detects numeric digits
- 🔣 Detects special characters
- 🟢 Rates password as Strong, Medium, or Weak

## Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- Regular Expressions (`re`)

## Project Structure

```
Password-Strength-Checker/
│── main.py
│── password_checker.py
└── README.md
```

## Concepts Practiced

- Classes and Objects
- Constructors (`__init__`)
- Methods
- Regular Expressions
- Conditional Statements
- String Manipulation

## How to Run

```bash
python main.py
```

## Example

**Input**

```
Python@123
```

**Output**

```
Password Strength: Strong
```

## Future Improvements

- Show estimated password entropy
- Detect repeated or sequential characters
- Check against a list of common passwords
- Suggest improvements for weak passwords
- Generate secure random passwords
