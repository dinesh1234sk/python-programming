import pandas as pd
#Create the DataFrame
data= pd.DataFrame ({
"Department": ["IT", "Finance", "IT", "HR", "Finance", "IT"],
    "Employee": ["Alice", "Bob", "Charlie", "David", "Eva", "Frahk"],
    "Salary": [60000, 70000, 80000, 55000, 65000,75000]
})
print(data)
grouped_salary = data.groupby("Department")["Salary"].sum()
print(grouped_salary)
average_salary = data.groupby ("Department") ["Salary"].mean()
print(average_salary)
max_salary = data.groupby ("Department") ["Salary"].max()
print(max_salary)
min_salary = data.groupby("Department") ["Salary"].min()
print(min_salary)
employee_count = data.groupby ("Department") ["Employee"].count()
print(employee_count)
multi_agg = data.groupby("Department") ["Salary"].agg(["sum", "mean", "max", "min", "count"])
print(multi_agg)