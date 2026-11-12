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


print('\n=== DataFrame에서 특정 행을 선택하는 방법 2가지 ===')
# iloc : '위치(Position)'로 선택(0번째, 1번째 처럼 순서/번호 접근)
# loc : '라벨(Label)'로 선택(index에 붙어있는 이름으로 접근)
'''
* iloc
iloc은 index의 '값'이 뭐든 상관 없이, '몇 번째 줄이냐'로 가져옴
ex) df.iloc[0] => 첫 번째 행(0번 위치)
'''
print(df.iloc[0])
print(df.iloc[1])
print(df.iloc[2])

'''
* loc
loc은 'index 라벨'로 접근
index를 '이름'으로 바꾸면(ex : Name열을 index로 지정)
df.index = ['사람1', '사람2', '사람3']
df.loc['사람1']로 접근
'''
print(df.loc[0])
print(df.iloc[0])


print('\n=== 상위/하위 데이터 출력 ===')
# head() : 위쪽(처음 부분) 몇 개의 행만 보여주는 함수
# tail() : 아래쪽(마지막 부분) 몇 개의 행만 보여주는 함수

# 상위 5개
print(df.head())
# 상위 2개
print(df.head(2))

# 하위 5개
print(df.tail())
# 하위 2개
print(df.tail(2))


print('\n=== 열 수정 ===')
# 새로운 열 추가
df['Survived'] = [0, 1, 1]
print(df)

# 열 이름 바꾸기
df = df.rename(columns={'Sex' : 'Gender'})
print(df)

# 열 삭제하기(axis=1 : 열 / axis=0 : 행)
df = df.drop('Survived', axis=1)
print(df)


print('\n=== 결측치(NaN) 처리 ===')
# 결측치란 값이 비어있는 상태
# pandas에서는 보통 NaN(Not of Number)으로 표시
# None을 넣어도 pandas에서는 자동으로 NaN으로 변환

print(df)
print(df.isnull())

df2 = df.copy()
# copy() : 원본 df를 복제

df2.loc[1, 'Age'] = None
print(df2.isnull())
# loc[행 라벨, 열이름]형태로 특정 위치의 값을 바꿀 수 있음

print(df2.dropna(axis=0))
# dropna() : 결측치가 있는 부분 제거

print(df2.fillna(0))
# fillna(i) : 결측치를 i값으로 채우기

print(df2['Age'].fillna(df['Age'].mean))
# 결측치를 평균 값으로 채우기

# print(df2.fillna(method='ffill')) // 이전 버전
print(df2.ffill())
# ffill : foward / 바로 위(이전 행)의 값으로 NaN 채움

# print(df2.fillna(method='bfill')) // 이전 버전
print(df2.bfill())
# bfill : backward / 바로 아래(다음 행)의 값으로 NaN 채움