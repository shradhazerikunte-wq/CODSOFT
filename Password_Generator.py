def main():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    
    print("Welcome to the Password Generator!")
    
    while True:
        try:
            length = int(input("Enter the desired length of the password (min 8): "))
            if length >= 8:
                break
            else:
                print("Password length must be at least 8.")
        except ValueError:
            print("Invalid input. Please enter a number.")
            
    password = ""
    index = 0
    
    for i in range(length):
        password += characters[index]
        index = (index + 7) % len(characters)
        
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()