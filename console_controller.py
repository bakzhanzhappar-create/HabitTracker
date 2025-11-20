from entities import Habit


class ConsoleController:
    __MIN_MINUTES: int = 0
    __MAX_MINUTES: int = 500
    __LOWEST_WEIGHT: int = 1
    __HIGHEST_WEIGHT: int = 10

    def __init__(self) -> None:
        ...

    def request_id(self) -> int:
        while True:
            habit_id: str = input("Enter ID of the habit you want to delete: ").strip()
            if self._validate_id(habit_id):
                return int(habit_id)

            else:
                print("Invalid ID")

    def request_command(self) -> str:
        while True:
            command: str = input(
                "\nType 'check' to view, 'delete' to remove, 'add' to add more, or 'exit' to quit: ").strip().lower()

            if self._validate_command(command):
                return command

            else:
                print("\nInvalid command. Please try again.")

    def request_habit(self) -> Habit | None:
        while True:
            print("====APPENDING====")
            habit_name = input("Habit name? ").strip()
            minutes: int = int(input("How many minutes?"))

            if not self._validate_minutes(minutes):
                print("Invalid minutes!")

            weight: int = int(input("Rate from 1 to 10, how important?"))

            if not self._validate_weight(weight):
                print("Invalid weight!")

            return Habit(
                name=habit_name,
                minutes=minutes,
                weight=weight,
            )

    def _validate_minutes(self, minutes: int) -> bool:
        return self.__MIN_MINUTES < minutes <= self.__MAX_MINUTES

    def _validate_weight(self, weight: int) -> bool:
        return self.__LOWEST_WEIGHT <= weight <= self.__HIGHEST_WEIGHT

    def _validate_command(self, command: str) -> bool:
        available_commands: list[str] = ["add", "delete", "check", "exit"]
        return command in available_commands

    def _validate_id(self, habit_id: str) -> bool:
        return habit_id.isdigit()
