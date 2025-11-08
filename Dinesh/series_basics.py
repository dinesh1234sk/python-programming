
import pandas as pd
print(pd.Series([10,20,30,40]))
marks = pd.Series([0,80,85],index = ["Alice", "Bob", "Charlie"])
print(marks)
print(marks ["Bob"])
print(marks + 5)
print("Average marks:", marks.mean())
print("Total marks:", marks.sum())
print("Highest mark:", marks.max())
student_marks = pd.Series({"Alice": 90, "Bob": 80, "Charlie": 85})
print(student_marks)
print(student_marks["Charlie"])