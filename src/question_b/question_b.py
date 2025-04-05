def get_day_of_week(day):
    days_of_week = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    
    if day in days_of_week:
        return days_of_week[day]
    else:
        return "Error: Invalid number! Please enter a number between 1 and 7."
