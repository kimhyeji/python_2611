import pandas as pd
# pandas : 파이썬에서 데이터 분석과 데이터 처리를 위한 대표적인 라이브러리
# 주로 표 형태의 데이터(엑셀, CSV, 데이터베이스 등)를 다루는 데 사용
# 데이터 과학, 머신러닝, 금융 분석, 통계 처리 등에서 매우 많이 사용 됨
'''
DataFrame : 여러 개의 열(Colum)로 구성된 '표'형태의 데이터
 - '열 이름': [값들]
 - 각 열에는 열 이름이 있음
 - 각 행에는 자동으로 행 번호(index)가 붙음
'''

df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)

print('=== 전체 출력 ===')
print(df)


print('\n=== 열 하나씩 출력 ===')
# 결과는 DataFrame이 아니라, 'Series'라는 1차원 자료구조로 나옴
print(df['Name'])
print(df['Age'])
print(df['Sex'])


print('\n=== 타입 출력 ===')
print(type(df))
print(type(df['Age']))


print('\n=== 이름이 Age인 Series 생성 ===')
ages = pd.Series([22, 35, 44], name='Age')
print(ages)


print('\n=== DataFrame에서 특정 열 꺼내기 ===')
print(df['Age'])


print('\n=== 기본 통계 함수 ===')
print('max : 최댓값')
print('최대 나이 : ', df['Age'].max())

print('min : 최솟값')
print('최소 나이 : ', df['Age'].min())

print('mean : 평균값')
print('평균 나이 : ', df['Age'].mean())

print('요약 통계 정보 보기')
# describe : 숫자형 열에 대해 '요약 통계 정보'를 한 번에 보여줌
print(df.describe())
'''
count   3.000000 : 데이터 개수
mean   38.333333 : 평균
std    18.230012 : 표준 편차(데이터가 평균에서 얼마나 퍼져 있는지)
min    22.000000 : 최솟값
25%    28.500000 : 1사분위수(Q1)
50%    35.000000 : 중앙값(median)
75%    46.500000 : 3사분위수(Q3)
max    58.000000 : 최댓값
'''

print('DataFrame의 전체 요약 정보')
# info : DataFrame의 '구조 정보'를 보여줌
print(df.info())