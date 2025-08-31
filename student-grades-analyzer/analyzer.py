"""
STUDENT GRADES ANALYZER 

WHAT THIS PROGRAM DOES:
Reads a CSV file of student names and scores, then prints:
- The average score
- The top scorer (name + score)

HOW TO RUN:
    python analyzer.py grades.csv

HOW IT WORKS (step-by-step):
1) Opens the CSV and reads each row as a dict (with keys "name" and "score").
2) Builds a Python dict {name: score} so it’s easy to calculate stats.
3) Uses statistics.mean(...) for the average.
4) Uses max(..., key=...) to find the highest score and who it belongs to.

WHAT I SHOULD NOTICE:
- Dicts (key → value) are convenient for “lookups” and aggregations.
- CSV is a super common format in consulting and data work.
"""

import csv, sys, statistics

def analyze(file):
    with open(file) as f:
        reader=csv.DictReader(f)
        scores={row["name"]:int(row["score"]) for row in reader}
    avg=statistics.mean(scores.values())
    top=max(scores,key=scores.get)
    print("Average:",avg)
    print("Top:",top,scores[top])

if __name__=="__main__":
    if len(sys.argv)<2:
        print("Usage: python analyzer.py file.csv")
    else:
        analyze(sys.argv[1])
