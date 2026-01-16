from append_habit import add_habit
from delete_habit_m import delete
from habits_reader import reader
from entities import Habit, WeightenedHabit
from console_controller import ConsoleController

console = ConsoleController()


def add_habits_ui():
    habit = console.request_habit()
    add_habit(habit)


def check_habits_ui():
    rows = reader()
    console.show_habits(rows)


def delete_habit_ui(id_to_delete):
    rows = reader()

    if not rows:
        console.show_error("No habits to delete.")
        return

    delete(id_to_delete)
    console.show_deleted(id_to_delete)

    # show updated list
    rows = reader()
    console.show_habits(rows)


def graceful_exit():
    console.show_goodbye()
    exit()


def main():
    console.show_goodbye()  # приветствие можно заменить

    while True:
        request = console.request_command()

        if request == "check":
            check_habits_ui()

        elif request == "delete":
            habit_id = console.request_id()
            delete_habit_ui(habit_id)

        elif request == "add":
            add_habits_ui()

        elif request == "exit":
            graceful_exit()

class User:

    """
    Class User implements a basic user interface, some methods related to creating a habit and providing basic operations.

    Operations include:
        Create a new habit
        Update an existing habit
        Delete an existing habit
        Retrieve all habits
        Retrieve one habit by habit_id

    """

    def __init__(self):
        ...


    def create_habit(self, name: str, time: int) -> Habit:
        habit: Habit = Habit(
            name=name,
            minutes=time,
        )

        return habit

    def create_weightened_habit(self, name: str, time: int, weight: int) -> WeightenedHabit:
        weightened_habit: WeightenedHabit = WeightenedHabit(
            name=name,
            minutes=time,
            weight=weight,
        )

        return weightened_habit



if __name__ == "__main__":
    # main()
    user: User = User()

    habit: Habit = user.create_habit(
        name="programming",
        time=20,
    )

    print(habit)