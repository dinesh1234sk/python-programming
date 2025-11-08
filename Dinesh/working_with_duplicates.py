import pandas as pd
# Create sample DataFrame with duplicates
data= pd.DataFrame({
"Department": ["IT", "Finance", "IT", "HR", "Finance", "IT", "IT", "HR"], "Employee": ["Alice", "Bob", "Charlie", "Alice", "Eva", "Frank", "Alice", "Alice"], "Salary": [60000, 70000, 80000, 60000, 65000,75000, 60000, 60000]
})
print(data)
print(data.duplicated())
duplicates = data[data.duplicated()]
print(duplicates)
duplicates = data[data.duplicated()]
print(duplicates)
cleaned_data = data.drop_duplicates()
print(cleaned_data)
keep_last = data.drop_duplicates (keep="last")
print(keep_last)
employee_duplicates = data.duplicated (subset=["Employee"])
print(employee_duplicates)
unique_employees= data.drop_duplicates (subset=["Employee"])
print(unique_employees)