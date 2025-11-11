import csv
from append_habit import add_habit
from delete_habit_m import delete
from entities import Habit
from habits_reader import reader

FILENAME = "habits.csv"


def add_habits_ui():
    while True:
        print("====APPENDING====")
        habit_name = input("Habit name? ").strip()
        minutes: int = int(input("How many minutes?"))
        while True:
            weight: int = int(input("Rate from 1 to 10, how important?"))
            if 1 <= weight <=10:
                break
            print("Weight must be between 1 and 10")
        add_habit(Habit(habit_name, minutes, weight))
        break

def check_habits_ui():
    print("\nTracks of Habits: ")
    reader(show=True)

def delete_habit_ui(id_to_delete):
    rows=reader()
    if not rows:
        print("No habits to delete")
        return
    delete(id_to_delete)
    print(f"Habit ID {id_to_delete} is deleted")
    reader(show=True)

def graceful_exit():
    print("Thanks to testing my project!\n =)")
    exit()

def main():
    print("это моя программа трекера")

    while True:
        request = input("\nType 'check' to view, 'delete' to remove, 'add' to add more, or 'exit' to quit: ").strip().lower()
        if request == "check":
            check_habits_ui()
        elif request == "delete":
            try:
                id_to_delete = int(input("Enter ID of the habit you want to delete: ").strip())
                delete_habit_ui(id_to_delete)
            except ValueError:
                print("Invalid ID. `RITE A NUMBA NIGGA")
        elif request == "add":
            add_habits_ui()
        elif request == "exit":
            graceful_exit()
        else:
            print("That's not a command!")

if __name__ == "__main__":
    main()