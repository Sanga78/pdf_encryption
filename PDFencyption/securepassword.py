import msvcrt
import sys

def password_contains_required_elements(password):
    # Checks for each requirement in the password
    has_digit = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    special_characters = set("!@#$%^&*()-_=+[]{}|;:',.<>/?`~")
    has_special = any(char in special_characters for char in password)
    
    return has_digit and has_upper and has_lower and has_special

def get_secure_password(prompt="Password: "):
    while True:
        sys.stdout.write(prompt)
        sys.stdout.flush()
        password = ""
        while True:
            key = msvcrt.getch()  # Get a single character without echo
            if key == b'\r':  # Return key pressed
                sys.stdout.write('\n')
                break
            elif key == b'\x08':  # Backspace key pressed
                if len(password) > 0:
                    password = password[:-1]
                    sys.stdout.write('\b \b')  # Move cursor back, print space to delete, move back again
                    sys.stdout.flush()
            else:
                password += key.decode('utf-8')
                sys.stdout.write('*')
                sys.stdout.flush()

        if password_contains_required_elements(password):
            return password
        else:
            print("Password is not strong enough.")
            confirm = input("Continue with this password? (Y/N): ")
            if confirm.lower() == 'y':
                return password
            # If 'n', the loop will continue, prompting for a new password

