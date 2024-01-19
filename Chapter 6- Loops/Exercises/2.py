while True:
    try:
        age = int(input("Enter your age (or type 'quit' to exit): "))
        
        if age < 3:
            print("Your ticket is free.")
        elif 3 <= age <= 12:
            print("Your ticket costs $10.")
        elif age > 12:
            print("Your ticket costs $15.")
        else:
            print("Invalid age entered. Please enter a valid age.")
    except ValueError:
        command = input("Invalid input. Do you want to quit? (yes/no): ").lower()
        if command == 'yes':
            break
