from typing import List

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from append_habit import add_habit
from delete_habit_m import delete
from habits_reader import reader
from entities import Habit


class HabitIn(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)
    minutes: int = Field(..., gt=0, le=50)
    weight: float = Field(..., ge=1, le=10)


class HabitOut(BaseModel):
    id: int
    name: str
    minutes: int
    weight: float
    date: str


app = FastAPI(title="Habit Tracker API")


@app.get("/habits", response_model=List[HabitOut])
def get_habits() -> List[HabitOut]:
    rows = reader(show=False)
    habits: List[HabitOut] = []
    for row in rows:
        # row format: [id, name, minutes, weight, date]
        if not row or len(row) < 5:
            continue
        habits.append(
            HabitOut(
                id=int(row[0]),
                name=row[1],
                minutes=int(float(row[2])),
                weight=float(row[3]),
                date=row[4],
            )
        )
    return habits


@app.post("/habits", response_model=HabitOut, status_code=201)
def create_habit(habit_in: HabitIn) -> HabitOut:
    habit = Habit(
        name=habit_in.name,
        minutes=habit_in.minutes,
        weight=habit_in.weight,
    )
    result = add_habit(habit)
    if result is False:
        raise HTTPException(status_code=500, detail="Storage file not found")

    rows = reader(show=False)
    if not rows:
        raise HTTPException(status_code=500, detail="Failed to read habits after insert")

    last = rows[-1]
    return HabitOut(
        id=int(last[0]),
        name=last[1],
        minutes=int(float(last[2])),
        weight=float(last[3]),
        date=last[4],
    )


@app.delete("/habits/{habit_id}", status_code=204)
def delete_habit(habit_id: int) -> None:
    rows = reader(show=False)
    if not any(row and int(row[0]) == habit_id for row in rows):
        raise HTTPException(status_code=404, detail="Habit not found")

    delete(habit_id)


app.mount(
    "/",
    StaticFiles(directory="static", html=True),
    name="static",
)


