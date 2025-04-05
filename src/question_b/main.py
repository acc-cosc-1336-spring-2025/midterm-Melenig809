from question_b import get_day_of_week 

def main():
    while True:
        user_input = input("Enter a number (1-7) to get the corresponding day of the week, or type 'quit' to exit: ")
        
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        
        try:
            day_number = int(user_input)
            
            result = get_day_of_week(day_number)
            print(result)
        
        except ValueError:
            print("Invalid input! Please enter a valid number between 1 and 7, or 'quit' to exit.")

if __name__ == "__main__":
    main()
