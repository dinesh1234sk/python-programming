import pandas as pd
data = pd.read_csv("employees.csv")
print(data)
data=pd.read_csv("employees.csv", index_col="Employee")
print(data)
data=pd.read_csv("employees.csv", usecol = ["Employee","salary"])
print(data)
for chunk in pd.read_csv("employees.csv", chunksize=2):
    print(chunk)