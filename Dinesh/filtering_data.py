import pandas as pd
#Create DataFrame
data =  pd.DataFrame({
"Department": ["IT", "Finance", "IT", "HR", "Finance", "IT"], "Employee": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
"Salary": [60000, 70000, 80000, 55000, 65000,75000],
"Bonus": [5000, 6000, 7000, 4000, 5000, 6000]
})
print(data)
#Single condition: Salary > 70000
high_salary = data[data["Salary"] > 70000]
print(high_salary)
#Multiple conditions: IT department and Salary > 60000
it_high_salary = data[(data["Department"] == "IT") & (data["Salary"] > 60000)]
print(it_high_salary)
# OR condition: Finance department or Salary > 75000
finance_or_high = data[(data["Department"] == "Finance") | (data["Salary"] > 75000)]
print(finance_or_high)
#isin() method
selected_departments = data[data["Department"].isin(["IT", "HR"])]
print(selected_departments)
#between method filter range
salary_range = data[data["Salary"].between (60000, 75000)]
print(salary_range)
# query method
finance_bonus = data.query("Department == 'Finance' and Bonus > 5000")
print(finance_bonus)