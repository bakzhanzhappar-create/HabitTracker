from entities import Habit


class ConsoleController:
    __MIN_MINUTES: int = 0
    __MAX_MINUTES: int = 50
    __LOWEST_WEIGHT: int = 1
    __HIGHEST_WEIGHT: int = 10

    def __init__(self) -> None:
        ...

    def request_id(self) -> int:
        while True:
            habit_id: str = input("Enter ID of the habit you want to delete: ").strip()

            if self._validate_id(habit_id):
                return int(habit_id)

            self.show_error("Invalid ID")

    def request_command(self) -> str:
        while True:
            command: str = input(
                "\nType 'check' to view, 'delete' to remove, 'add' to add more, or 'exit' to quit: ").strip().lower()

            if self._validate_command(command):
                return command

            self.show_error("Invalid command. Please try again.")

    def request_habit(self) -> Habit | None:

        while True:
            habit_name = input("Habit name? ").strip()
            minutes: int = int(input(f"How many minutes? ({self.__MIN_MINUTES}–{self.__MAX_MINUTES}): "))

            if not self._validate_minutes(minutes):
                self.show_error("Invalid minutes!")
                continue

            weight: int = int(input("Rate from 1 to 10, how important? "))

            if not self._validate_weight(weight):
                self.show_error("Invalid weight!")
                continue

            return Habit(name=habit_name, minutes=minutes, weight=weight)

    def show_habits(self, rows: list[list[str]]) -> None:
        if not rows:
            print("No tracks. Add a habit first.")
            return

        print("\nTracks of Habits:\n")
        for row in rows:
            print(f"{row[0]} | Habit {row[1]} | min: {row[2]} | importance: {row[3]} | Date: {row[4]}")

    def show_deleted(self, habit_id: int):
        print(f"Habit ID {habit_id} is deleted.")

    def show_goodbye(self):
        print("Thanks for testing my project! =)")

    def show_error(self, text: str):
        print(f"[ERROR] {text}")

    def _validate_minutes(self, minutes: int) -> bool:
        return self.__MIN_MINUTES < minutes <= self.__MAX_MINUTES

    def _validate_weight(self, weight: int) -> bool:
        return self.__LOWEST_WEIGHT <= weight <= self.__HIGHEST_WEIGHT

    def _validate_command(self, command: str) -> bool:
        return command in ["add", "delete", "check", "exit"]

    def _validate_id(self, habit_id: str) -> bool:
        return habit_id.isdigit()
