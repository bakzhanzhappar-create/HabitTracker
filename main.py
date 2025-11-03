import csv
from append_habit import add_habit
from delete_habit_m import delete

FILENAME = "habits.csv"


def add_habits_ui():
    while True:
        print("====APPENDING====")
        habit_name = input("Habit name? ").strip()
        minutes: int = int(input("How many minutes?"))
        habit_id=add_habit(habit_name,minutes)
        print(f"Habit ID is {habit_id}")
        break

def check_habits():
    print("\n Tracks of Habits: ")
    try:
        with open(FILENAME, mode="r", newline='', encoding="utf-8")as file:
            reader=list(csv.reader(file))
            if reader:
                for row in reader:
                    print(f"{row[0]}| Habit {row[1]} | min: {row[2]} | Date: {row[3]}")
            else:
                print(f"No entries yet.")

    except FileNotFoundError:
        print("No tracks. Add a habit")

def delete_habit_ui(id_to_delete):
    try:
        with open(FILENAME, mode="r", newline='', encoding="utf-8")as file:
            rows = list(csv.reader(file))
            if not rows:
                print("No habits to delete")
                return
    except FileNotFoundError:
        print("No tracks. Add a habit")
        return
    print(f"Habit ID is {id_to_delete}")

def graceful_exit():
    print("Thanks to testing my project!\n =)")
    exit()
def main():

    print("это моя программа трекера")

    while True:
        request = input("\nType 'check' to view, 'delete' to remove, 'add' to add more, or 'exit' to quit: ").strip().lower()
        if request == "check":
            check_habits()
        elif request == "delete":
            try:
                id_to_delete = int(input("Enter ID of the habit you want to delete: ").strip())
                delete(id_to_delete)
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