import pandas as pd
data = pd.DataFrame({
"Name": ["Alice", "Bob", "Charlie", "David"],
"Age": [24, 22, 23, 21],
"Marks": [85, 92, 78, 88]
})
print(data)
print(data.head())
print(data.tail())
print(data["Name"])
print(data["Marks"])
print(data[["Name", "Marks"]])
print(data.shape)
print(data.size)
print(data.info())
#Access a single row using loc
print(data.loc[0]) # 1st row
print(data.loc[[1,2]])
#iloc
print(data.iloc[:2])
# Filter students with marks > 85
high_scorers = data[data ["Marks"] > 85]
print(high_scorers)
#Filter with multiple conditions
filtered_data = data[(data["Marks"] > 80) & (data["Age"] <24)]
print (filtered_data)
#Sort by marks in descending order
sorted_data = data.sort_values(by="Marks", ascending=False)
print(sorted_data)
# Descriptive statistics
print(data.describe())