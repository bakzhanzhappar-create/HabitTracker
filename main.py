import csv
from datetime import datetime
from fileinput import close

FILENAME = "habits.csv"


def add_habits():
    while True:
        habit = input("Habit name? ").strip()
        minutes = int(input("How many minutes?"))
        try:
            with open(FILENAME, mode="r", newline='', encoding="utf-8") as file:
                reader = list(csv.reader(file))
                habit_id=len(reader)+1
            close()

        except FileNotFoundError:
            habit_id=1

        now=datetime.now().date()
        with open(FILENAME, mode="a", newline='', encoding="utf-8") as file:
            writer=csv.writer(file)
            writer.writerow([habit_id, habit, minutes, str(now)])

        print(f"Habit '{habit}' saved with ID {habit_id}")
        close()
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
        close()

    except FileNotFoundError:
        print("No tracks. Add a habit")

def delete_habit(id):
    try:
        with open(FILENAME, mode="r", newline='', encoding="utf-8")as file:
            rows = list(csv.reader(file))
            if not rows:
                print("No habits to delete")
                return

            for row in rows:
                print(f"ID: {row[0]} | Habit {row[1]} | m: {row[2]} | Date: {row[3]}")
    except FileNotFoundError:
        print("No tracks. Add a habit")
        close()
        return

    new_rows=[row for row in rows if row and int(row[0]) != id]
    with open(FILENAME, mode="w", newline='', encoding="utf-8")as file:
        writer=csv.writer(file)
        writer.writerows(new_rows)
    print(f"Habit with ID {id} deleted")
    close()

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
            id_to_delete = int(input("Enter ID of the habit you want to delete: ").strip())
            delete_habit(id_to_delete)
        elif request == "add":
            add_habits()
        elif request == "exit":
            graceful_exit()
        else:
            print("That's not a command!")

if __name__ == "__main__":
    main()