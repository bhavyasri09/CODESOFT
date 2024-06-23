import random
import string

def generate_password(length):
    if length < 1:
        return "Error! Password length must be at least 1."

  
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

 
    all_characters = lower + upper + digits + symbols


    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def main():
    print("Password Generator")
    
    try:
        length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Invalid input! Please enter a numeric value.")
        return

    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
