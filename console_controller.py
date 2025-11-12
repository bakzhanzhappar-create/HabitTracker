from entities import Habit

class ConsoleController:
    __MIN_MINUTES: int = 0
    __MAX_MINUTES: int = 500
    __LOWEST_WEIGHT: int = 1
    __HIGHEST_WEIGHT: int = 10

    def __init__(self) -> None:
        ...

    def request_habit(self) -> Habit | None:
        while True:
            print("====APPENDING====")
            habit_name = input("Habit name? ").strip()
            minutes: int = int(input("How many minutes?"))

            if not self._validate_minutes(minutes):
                print("Invalid minutes!")
                break

            weight: int = int(input("Rate from 1 to 10, how important?"))

            if not self._validate_weight(weight):
                print("Invalid weight!")
                break

            return Habit(
                name=habit_name,
                minutes=minutes,
                weight=weight,
            )

    def _validate_minutes(self, minutes: int) -> bool:
        return self.__MIN_MINUTES < minutes <= self.__MAX_MINUTES

    def _validate_weight(self, weight: int) -> bool:
        return self.__LOWEST_WEIGHT <= weight <= self.__HIGHEST_WEIGHT