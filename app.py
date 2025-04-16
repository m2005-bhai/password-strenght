import re

def check_password_strength(password):
    strength = 0
    remarks = ""

    # Length check
    if len(password) >= 8:
        strength += 1
    # Upper and lower case check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        strength += 1
    # Digit check
    if re.search(r"\d", password):
        strength += 1
    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1

    if strength == 4:
        remarks = "Strong password 💪"
    elif strength == 3:
        remarks = "Moderate password 🙂"
    elif strength == 2:
        remarks = "Weak password 😕"
    else:
        remarks = "Very weak password 😢"

    return remarks

# Example
password = input("Enter your password: ")
print(check_password_strength(password))
