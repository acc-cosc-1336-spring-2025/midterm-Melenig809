from question_d import get_miles_per_hour

def main():
    try:
        kilometers = int(input("Enter the number of kilometers: "))
        minutes = int(input("Enter the number of minutes: "))
        
        result = get_miles_per_hour(kilometers, minutes)
        
        print(f"The speed is: {result} miles per hour.")
    
    except ValueError:
        print("Invalid input! Please enter valid integers for kilometers and minutes.")

if __name__ == "__main__":
    main()
