import pandas as pd
import matplotlib.pyplot as plt

# temps = [13, 14, 16, 18, 17, 15]
# df = pd.DataFrame({"temp": temps})
# df["temp"].plot(title="Hourly Temp")

# plt.show()

df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
# grp = df.groupby("Pclass")["Fare"].mean()

# grp.plot(kind="bar", title="Average Fare by Pclass")

# bins = [0, 10, 20, 30, 40, 50, 60, 70, 80]
# names = ["0대", "10대", "20대", "30대", "40대", "50대", "60대", "70대+"]
# df["연령대"] = pd.cut(df["Age"], bins=bins, labels=names)

# grp = df.groupby("연령대")["Survived"].mean()
# grp.plot(kind="bar", title="Survival by Age Group")
# plt.show()

# df["Age"].plot(kind="hist", title="Age Distribution")
# plt.show()

df.groupby(["Sex", "Pclass"])["Survived"].mean().plot(kind="bar", title="Survival Rate by Pclass")
plt.tight_layout()
plt.show()

print("수정본")

# plt.show()