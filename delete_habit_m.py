import csv

FILENAME="habits.csv"

def delete(id_to_delete):
    with open(FILENAME, mode="r", newline='', encoding="utf-8") as file:
        rows = list(csv.reader(file))
    new_rows=[row for row in rows if row and int(row[0]) != id_to_delete]

    with open(FILENAME, mode="w", newline='', encoding="utf-8")as file:
        writer=csv.writer(file)
        writer.writerows(new_rows)