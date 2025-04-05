from question_c import get_sum_of_evens

def main():
    while True:
        user_input = input("Enter a number to get the sum of even numbers (or type 'quit' to exit): ")
        
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        
        try:
            num = int(user_input)
            
            total = get_sum_of_evens(num)
            print(f"The sum of even numbers from 1 to {num} is: {total}")
        
        except ValueError:
            print("Invalid input! Please enter a valid number or 'quit' to exit.")

if __name__ == "__main__":
    main()
