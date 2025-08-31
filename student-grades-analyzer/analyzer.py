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
