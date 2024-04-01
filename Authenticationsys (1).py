def count_characters(s):
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    return counts

def has_consecutive_sequence(s, username):
    for i in range(len(s) - 2):
        if s[i:i+3] in username:
            return True
    return False

def has_repeating_characters(s):
    for i in range(len(s) - 3):
        if s[i] == s[i+1] == s[i+2] == s[i+3]:
            return True
    return False

def validate_password(password, username, last_three_passwords):
    
    if len(password) < 10:
        return False, "Password must be at least 10 characters long."

    upper_count = sum(1 for char in password if char.isupper())
    if upper_count < 2:
        return False, "Password must contain at least two uppercase letters."

    lower_count = sum(1 for char in password if char.islower())
    if lower_count < 2:
        return False, "Password must contain at least two lowercase letters."

    digit_count = sum(1 for char in password if char.isdigit())
    if digit_count < 2:
        return False, "Password must contain at least two digits."

    special_count = sum(1 for char in password if not char.isalnum())
    if special_count < 2:
        return False, "Password must contain at least two special characters."

    if has_consecutive_sequence(password, username):
        return False, "Password cannot contain three or more consecutive characters from the username."
    if has_repeating_characters(password):
        return False, "Password cannot contain a character repeating more than three times in a row."

    if password in last_three_passwords:
        return False, "Password cannot be the same as any of the last three passwords."

    return True, "Password is valid."

def main():
    username = input("Enter your username: ")
    last_three_passwords = []

    while True:
        password = input("Enter your new password: ")

        is_valid, message = validate_password(password, username, last_three_passwords)
        if is_valid:
            print("Password is valid.")
            break
        else:
            print("Password is invalid:", message)

    last_three_passwords.append(password)
    if len(last_three_passwords) > 3:
        last_three_passwords.pop(0)

if __name__ == "__main__":
    main()
