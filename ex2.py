import pandas as pd

df = pd.read_csv("employees.csv")

print(df)

df["부서"] = df["부서"].fillna(df["부서"].mode()[0])

df["연봉"] = df["연봉"].fillna(df["연봉"].mean())

df = df.drop(columns=["비고"])

print(df.isnull().sum())