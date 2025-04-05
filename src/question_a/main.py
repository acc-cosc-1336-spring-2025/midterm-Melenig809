from question_a import is_prime 

def main():
    while True:
        user_input = input("Enter a number to check if it's prime (or type 'quit' to exit): ")
        
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        
        try:
            number = int(user_input)
            
            if is_prime(number):
                print(f"{number} is a prime number.")
            else:
                print(f"{number} is not a prime number.")
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
