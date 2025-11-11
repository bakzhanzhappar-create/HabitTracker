import csv

FILENAME='habits.csv'

def reader(show=False):
    try:
        with open(FILENAME, mode="r", newline='', encoding="utf-8")as file:
            readers=list(csv.reader(file))
            if not readers:
                if show:
                    print("No tracks.")
                return []
            if show:
                for row in readers:
                    print(f"{row[0]}| Habit {row[1]} | min: {row[2]} | importance: {row[3]} |Date: {row[4]} ")
            return readers
    except FileNotFoundError:
        if show:
            print("No tracks. Add a habit")
        return []