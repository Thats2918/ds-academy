import pandas as pd

# print("pandas 버전: " + pd.__version__)

# data = {
#     "이름": ["김데이터", "이분석", "박엔지"],
#     "점수": [90, 85, 95]
# }

data = {
    "이름": ["김철수","최민수","이영희","박영수","정민희"],
    "팀": ["A", "B", "A", "B", "A"],
    "점수": [90, 85, 95, 70, 88]
}

df = pd.DataFrame(data)

# 전체 내용 출력
# print(df)

# 한 열만
# print(df["점수"])

# 90점 이상만
# print(df[df["점수"] >= 90])

# 점수 높은 순으로 정렬
# print(df.sort_values("점수", ascending=False))

# 특정 그룹의 데이터 추출
# print(df.groupby("팀")["점수"].mean())

# 90점 이상인 등급 열 추가
df["등급"] = df["점수"].apply(lambda x: "우수" if x >= 90 else "보통")

df["보너스"] = df["점수"] * 0.1

df.to_csv("result.csv", index=False, encoding="utf-8-sig")
print("저장 완료!")

