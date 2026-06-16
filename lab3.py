import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# print(df.shape)
# print(df.head())

# print(df.info())
# print(df["Survived"].mean())


# print(df.isnull().sum())

# survived = df[df["Survived"] == 1]
# print(len(survived), "명 생존")

# print(df.groupby("Sex")["Survived"].mean())
# print(df.groupby("Pclass")["Survived"].mean())


# print(df.groupby(["Sex", "Pclass"])["Survived"].mean())

# df.groupby("Pclass")["Survived"].mean().plot(kind="bar")
# plt.title("Survival Rate by Class")
# plt.show()

# print(df[df["Age"] < 10]["Survived"].mean())

# print(df.groupby("Embarked")["Survived"].mean())

# print(df.groupby("Survived")["Fare"].mean())

