from dataclasses import dataclass


@dataclass
class Habit:
    name: str
    minutes: int

    def __repr__(self):
        return f"{Habit.__name__} consists of: '{self.name}' as name and {self.minutes} minutes"


@dataclass
class WeightenedHabit(Habit):
    weight: float
