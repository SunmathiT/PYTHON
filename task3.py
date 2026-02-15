import pandas as pd
df = pd.read_csv("data.csv")
df = pd.read_excel("data.xlsx")
df = pd.read_json("data.json")
df.head()
df.tail()
df.info()
df.describe()
df[df["Age"] > 25]
df[df["Salary"] >= 50000]
df[df["Gender"] == "Female"]
df[(df["Age"] > 25) & (df["Gender"] == "Male")]
df[(df["Salary"] > 40000) | (df["Department"] == "HR")]
df[["Name", "Age"]]
df[df["Department"].isin(["HR", "IT"])]
df[df["City"] != "Chennai"]
