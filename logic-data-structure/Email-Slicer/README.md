# 📧 Email Slicer (Python OOP)

A simple console-based Email Slicer built using Python and Object-Oriented Programming (OOP). The application separates an email address into its username and domain.

## Features

- 📧 Accept an email address as input
- 👤 Extract the username
- 🌐 Extract the domain
- ✅ Basic email validation

## Technologies Used

- Python 3
- Object-Oriented Programming (OOP)

## Project Structure

```
Email-Slicer/
│── main.py
│── email_slicer.py
└── README.md
```

## Concepts Practiced

- Classes and Objects
- Constructors (`__init__`)
- Methods
- String Manipulation
- String Splitting
- Input Validation

## How to Run

```bash
python main.py
```

## Example

**Input**

```
john.doe@gmail.com
```

**Output**

```
Username : john.doe
Domain   : gmail.com
```

## Future Improvements

- Validate email format using regular expressions (`re`)
- Extract top-level domain (e.g., `.com`, `.org`)
- Support multiple email addresses
- Save extracted information to a file
- GUI version using Tkinter