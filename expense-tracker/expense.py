"""WHAT THIS PROGRAM DOES:
Tracks simple expenses from the command line and saves them to a CSV file.

HOW TO USE (examples):
    python expense.py add Food 12.5
    python expense.py list

HOW IT WORKS (step-by-step):
1) "add <category> <amount>" → appends a new row [category, amount] to expenses.csv.
2) "list" → reads expenses.csv, prints each line, and sums the total.

WHAT I SHOULD NOTICE:
- CSV is easy to read and edit later in Excel/Google Sheets.
- I’m practicing file I/O (reading and writing files) and basic parsing of command-line inputs.
"""

import csv, sys, os

FILE="expenses.csv"

def add(category,amount):
    with open(FILE,"a",newline="") as f:
        writer=csv.writer(f)
        writer.writerow([category,amount])
    print("Added",category,amount)

def list_expenses():
    if not os.path.exists(FILE): return
    with open(FILE) as f:
        total=0
        for row in csv.reader(f):
            if not row: continue
            cat,amt=row[0],float(row[1])
            total+=amt
            print(cat,amt)
        print("Total:",total)

def main():
    if len(sys.argv)<2:
        print("Usage: add <cat> <amt> | list")
        return
    cmd=sys.argv[1]
    if cmd=="add":
        add(sys.argv[2],float(sys.argv[3]))
    elif cmd=="list":
        list_expenses()
    else:
        print("Unknown command")

if __name__=="__main__":
    main()
