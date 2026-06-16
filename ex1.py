import pandas as pd

df = pd.DataFrame({"이름": ["김","이","박","최","정","한"],
                   "부서": ["영업","개발","영업","개발","인사","개발"],
                   "연차": [3, 7, 5, 2, 8, 4],
                   "연봉": [4200, 6800, 5100, 3900, 7200, 5600]})

print(df[df["연봉"] >= 5000])

print(df.sort_values("연차", ascending=False))

print(df.groupby("부서")["연봉"].mean())

print(df.groupby("부서")["이름"].count())