"""
intermediate_notes.py : stepping up from beginner to intermediate Python.
"""
print("=== INTERMEDIATE PYTHON NOTES ===")

# Functions with *args, **kwargs
print("\n1) Functions with *args, **kwargs")
def demo(a, *args, **kwargs):
    print("a:", a)
    print("args:", args)
    print("kwargs:", kwargs)
demo(1,2,3,x=10,y=20)

# List & dict tricks
print("\n2) List & dict tricks")
nums = [5,2,9,1]
print("sorted:", sorted(nums))
squares = [n*n for n in nums]
print("squares:", squares)
grades = {"Ann":88,"Bo":92,"Cat":77}
for name,score in grades.items():
    print(name, score)

# JSON file
print("\n3) JSON file")
import json
data = {"user":"Bennett","score":95}
with open("data.json","w") as f: json.dump(data,f)
with open("data.json") as f: print("from file:", json.load(f))

# Exception with finally
print("\n4) try/except/finally")
try:
    val = 10/0
except ZeroDivisionError:
    print("divide by zero")
finally:
    print("cleanup done")

# Classes with inheritance
print("\n5) Classes + inheritance")
class Animal:
    def speak(self): return "sound"
class Dog(Animal):
    def speak(self): return "woof"
print(Dog().speak())

# Requests
print("\n6) Using requests (mock example)")
try:
    import requests
    r = requests.get("https://httpbin.org/get")
    print("status:", r.status_code)
except Exception as e:
    print("requests not installed or network issue")

# Pandas mini
print("\n7) pandas mini example")
try:
    import pandas as pd
    df = pd.DataFrame({"name":["Ann","Bo"],"score":[90,85]})
    print(df.describe())
except Exception as e:
    print("pandas not installed")

# unittest demo
print("\n8) unittest quick demo")
import unittest
class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(2+2,4)
if __name__=="__main__":
    unittest.main(exit=False)
