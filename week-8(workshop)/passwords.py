import re

def is_strong(password):
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    special_chars = "@#$ %&* "
    if not any(char in special_chars for char in password):
        return False  
    return True
weak_passwords = []
try:
    with open("passwords.txt", "r") as file:
        for line in file:
            pwd = line.strip()
            if not is_strong(pwd):
                weak_passwords.append(pwd) [cite: 18, 19]
    with open("weak.txt", "w") as output_file:
        for wp in weak_passwords:
            output_file.write(wp + "\n") [cite: 20]
    print(f"Audit complete. {len(weak_passwords)} weak passwords identified and saved.")
except FileNotFoundError:
    print("Error: passwords.txt not found. Please create the file first.")