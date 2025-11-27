import csv

FILENAME='habits.csv'

def reader(show=False):
    try:
        with open(FILENAME, mode="r", newline='', encoding="utf-8")as file:
            readers=list(csv.reader(file))
            if not readers:
                return []
            return readers
    except FileNotFoundError:
        return []