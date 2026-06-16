import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

first = df[df["Pclass"] == 1]
second = df[df["Pclass"] == 2]

upper = pd.concat([first, second], ignore_index=True)

# print(upper)

ports = pd.DataFrame({"Embarked": ["C", "Q", "S"], "항구명": ["Cherbourg", "Queenstown", "Southampton"]})

merged = pd.merge(df, ports, on="Embarked")

third = df[df["Pclass"] == 3]
whole = pd.concat([upper, third], ignore_index = True)

labels = pd.DataFrame({"Pclass": [1, 2, 3], "등급설명": ["1등급", "2등급", "3등급"]})

result = pd.merge(df, labels, on="Pclass")

print(result.groupby("등급설명")["Survived"].mean())


# print(merged[["Name", "Embarked", "항구명"]])