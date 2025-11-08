import pandas as pd
#Create DataFrame
data = pd.DataFrame({
"Department": ["IT", "Finance", "IT", "HR", "Finance", "IT"], "Employee": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"], "Salary": [60000, 70000, 80000, 55000, 65000, 75000], "Bonus": [5000, 6000, 7000, 4000, 5000, 6000]
})
print(data)
# Sort by salary ascending
sorted_salary = data.sort_values(by="Salary")
print(sorted_salary)
# Sort by salary descending
sorted_salary_desc= data.sort_values(by="Salary", ascending=False)
print(sorted_salary_desc)
# Sort by Multiple Columns: Department then Salary
sorted_dept_salary = data.sort_values(by=["Department", "Salary"])
print(sorted_dept_salary)