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
