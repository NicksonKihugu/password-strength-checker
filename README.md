PASSWORD-STRENGTH-CHECKER

DESCRIPTION:
This is a command-line Python program that evaluates the strength of a user's password based on common security criteria. 
If the password is deemed weak or moderate, the program suggests a stronger alternative using pattern-based generation.

FEATURES:
1. Prompts the user to enter a password
2. Validates minimum length (at least 8 characters)
3. Analyzes password strength based on:
    -> Uppercase letters
    ->Lowercase letters
    ->Digits
    ->Special characters
4. Classifies passwords into:
    i) Weak
    ii) Moderate
    iii) Strong
    iv) Very Strong
5. Suggests a stronger password when needed

HOW IT WORKS:
1. Input Validation
The program ensures the password is at least 8 characters long. If not, it exits immediately with:
   Short

2. Strength Evaluation
Using regular expressions, the program checks for the presence of:
    [A-Z] - Uppercase letters
    [a-z] - Lowercase letters
    \d - Digits
    \W - Special characters
Each category contributes 1 point to a total score (0–4).

3. Strength Classification
Score	Strength
4	Very strong
3	Strong
2	Moderate
0–1	Weak

5. Password Suggestion
If the password is Weak or Moderate, the program generates a suggestion using a predefined pattern:
    2 uppercase + 3 lowercase + 4 digits + 1 special character

REQUIREMENTS:
Python 3.x
exrex library
   -Install exrex using:
     -> pip install exrex

USAGE:
Run the program:
    python main.py

    Example:
    Enter your password: hello123
    Moderate
    Suggested Password: ABcde1234!

PROJECT STRUCTURE:
.
├── main.py
└── README.md

LIMITATIONS:
The strength check is based only on character variety, not real-world attack resistance
Does not check against common passwords or dictionary attacks
Suggested passwords follow a fixed pattern (not customizable)

FURTURE IMPROVEMENTS:
Add entropy-based strength calculation
Check passwords against known breached databases
Allow customizable password policies
Provide multiple suggestions instead of just one

AUTHOR:
Built as part of a learning project to explore:
Regular expressions
Password validation logic
Secure coding basics
