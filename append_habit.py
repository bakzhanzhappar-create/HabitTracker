import csv
from datetime import datetime

FILENAME="habits.csv"

def add_habit(habit_name, minutes):
    try:
        with open(FILENAME, "r", newline="", encoding="utf-8") as csvfile:
            reader=list(csv.reader(csvfile))
            habit_id=len(reader)+1
    except FileNotFoundError:
        return False

    now=datetime.now().date()
    with open(FILENAME, 'a', newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([habit_id, habit_name, minutes, str(now)])
        print(f"Habit '{habit_name}' saved with ID {habit_id}")
    return True
