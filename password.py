import exrex
import re
import sys


def main():
    # Prompt user for password
    password = input("Enter your password: ").strip()
    # Exit if password is less than 8 chars
    if len(password) < 8:
        sys.exit("Short")

    strength = password_check(password)
    
    if strength == "Weak" or strength == "Moderate":
        print(strength)
        suggest_password()
    else:
        print(strength)


def password_check(password):
    # Criteria for a strong password
    # ?= checks if sth exist in the string
    # .*[A-Z] if one or more character in A-Z are present
    # ? the group might or not be there 
    pattern = r"((?=.*[A-Z]))?((?=.*[a-z]))?((?=.*\d))?((?=.*\W))?"
    matches = re.search(pattern, password)

    # If a group exists it's counted
    score = 0
    for g in matches.groups():
        if g is not None:
            score += 1

    # Decision making
    if score == 4:
        return ("Very strong")
    elif score == 3:
        return ("Strong")
    elif score == 2:
        return ("Moderate")
    else:
        return "Weak"


def suggest_password():
    pattern = r"([A-Z]){2}([a-z]){3}(\d){4}(\W){1}"
    suggestion = exrex.getone(pattern)
    print(f"Suggested Password: {suggestion}")


if __name__ == "__main__":
    main()








