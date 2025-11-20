from dataclasses import dataclass


@dataclass
class Habit:
    name: str
    minutes: int
    weight: int