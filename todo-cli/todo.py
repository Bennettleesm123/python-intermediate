"""
EXPENSE TRACKER — SIMPLE EXPLANATION

WHAT THIS PROGRAM DOES:
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

import json, sys, os

FILE = "tasks.json"

def load():
    if not os.path.exists(FILE): return []
    with open(FILE) as f: return json.load(f)
def save(tasks):
    with open(FILE,"w") as f: json.dump(tasks,f,indent=2)

def list_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
    for i,t in enumerate(tasks,1):
        status = "✓" if t["done"] else " "
        print(f"{i}. [{status}] {t['text']}")

def main():
    tasks = load()
    if len(sys.argv)<2:
        print("Usage: add <task> | list | done <n>")
        return
    cmd = sys.argv[1]
    if cmd=="add":
        task=" ".join(sys.argv[2:])
        tasks.append({"text":task,"done":False})
        save(tasks)
        print("Added:",task)
    elif cmd=="list":
        list_tasks(tasks)
    elif cmd=="done":
        idx=int(sys.argv[2])-1
        if 0<=idx<len(tasks):
            tasks[idx]["done"]=True
            save(tasks)
            print("Done:",tasks[idx]["text"])
    else:
        print("Unknown command")

if __name__=="__main__":
    main()
