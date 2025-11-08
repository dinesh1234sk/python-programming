import pandas as pd
data = pd.DataFrame({
"Name": ["John", "Emma", "Sophia", "Michael", "David"],
    "Department": ["HR", "Finance", None, "IT", "Finance"],
    "Bonus": [5000, None, 3000, 4000, None],
"Salary": [50000, 65000, 58000, None, 70000],
})
print(data)
#isna
print(data.isna())
#Count missing values per column
print(data.isna().sum())
print(data.isna().any())
print(data.isna().all())
#Create a sample DataFrame with missing values
data = pd.DataFrame({
"Product": ["Laptop", "Smartphone", "Tablet", "Headphones", "Camera"],
"Category": ["Electronics", "Electronics", "Electronics", None, "Gadgets"],
"Price": [80000, 50000, 30000, 10000, None],
"Discount": [5000, None, 2000, None, 1000]
})
print(data)
# Fill missing discounts with 0
data["Discount"] = data["Discount"].fillna (0)
print(data)
data["Category"] = data["Category"].fillna ("Unknown")
print(data)
data["Price"] = data["Price"].fillna (data["Price"].mean())
print(data)
data["Discount"] = data["Discount"].replace(0, "No Discount")
print(data)
data = pd.DataFrame ({
"Product": ["Laptop", "Smartphone", "Tablet", "Headphones", "Camera"],
    "Category": ["Electronics", "Electronics", "Electronics", None, "Gadgets"],
    "Price": [80000, 50000, 30000, 10000, None],
"Discount": [5000, None, 2000, None, 1000]
})
print(data)
data.dropna(inplace=True)
print(data)
data = pd.DataFrame({
"Product": ["Laptop", "Smartphone", "Tablet", "Headphones", "Camera"], "Category": ["Electronics", "Electronics", "Electronics", None, "Gadgets"], "Price": [80000, 50000, 30000, 10000, None], "Discount": [5000, None, 2000, None, 1000]
})
print(data)
data.dropna (axis=1, inplace=True)
print(data)
data = pd.DataFrame({
"Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "Temperature": [30, None, 28, None, 32, None, 31]
})
print(data)
f_filled = data.ffill()
print(f_filled)
data = pd.DataFrame({
"Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "Temperature": [30, None, 28, None, 32, None, 31]
})
b_filled = data.bfill()
print(b_filled)
data = pd.DataFrame ({
"Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "Temperature": [30, None, None, None, None, None, 31]
})
limited_filled = data.ffill(limit=1)
print(limited_filled)