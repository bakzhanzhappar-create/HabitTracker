from append_habit import add_habit
from delete_habit_m import delete
from habits_reader import reader

from console_controller import ConsoleController

FILENAME = "habits.csv"

console = ConsoleController()

def add_habits_ui():
    habit = console.request_habit()
    add_habit(habit)


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
        request = console.request_command()
        if request == "check":
            check_habits_ui()

        elif request == "delete":
            id_to_delete = console.request_id()
            delete_habit_ui(id_to_delete)

        elif request == "add":
            add_habits_ui()

        elif request == "exit":
            graceful_exit()


if __name__ == "__main__":
    main()