import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

print(df.isnull().sum())

df["Age"] = df["Age"].fillna(df["Age"].mean())

print(df.isnull().sum())


print("제거 전: ", len(df))
df = df.drop_duplicates()
print("제거 후: ", len(df))


df["Age"] = df["Age"].astype(int)
print(df["Age"])

df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
df = df.drop(columns=["Cabin"])

print(df.isnull().sum())



# df["Pclass"] = df["Pclass"].astype(int)
# print(df["Pclass"].dtype)