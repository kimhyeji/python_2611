import re

print('==== 정규 표현식 ====')

# 일반 검색
text = '내 혈압은 120mmHg 입니다.'
print('120' in text)

# 정규표현식
pattern = r'\d+'
result = re.findall(pattern, text)
print(result)


print('==== 정규 표현식 : 기본 패턴 ====')
sample = 'abc123xyz456'

# 숫자 찾기
print(re.findall(r'\d+', sample))

# 문자 찾기
print(re.findall(r'[a-z]+', sample))

# + -> 1개 이상
# * -> 0개 이상
# ? -> 0개 또는 1개

print('==== 정규 표현식 : 특정 형식 찾기 ====')

data = '이메일은 test123@gmail.com 입니다.'

# 이메일 형식 간단히 찾기
email_pattern = r'\w+@\w+\.\w+'
emails = re.findall(email_pattern, data)
print(emails)

# \w -> 문자 또는 숫자
# @ -> @문자
# \. -> .은 정규식에서 특수 문자이기 때문에 \를 붙여야 함

print('==== 정규 표현식 : re모듈 주요 함수 ====')
# re.findall()
# re.search()
# re.match()
# re.fullmatch()
# re.sub()
# re.split()

text = 'python 123 java 456'
result = re.search(r'\d+', text)
print(result.group())


print('==== 정규 표현식 : 문자열 치환(replace 대신 re.sub) ====')

text2 = '가격은 12000원 입니다'

# 숫자 제거
new_text = re.sub(r'\d+', '', text2)
print(new_text)

print('==== 정규식 vs 일반 문자열 처리 비교 ====')

text3 = '몸무게: 70kg, 키: 170cm'

# 단순 split 사용
print(text3.split(','))

# 정규식으로 숫자만 추출
nums = re.findall(r'\d+', text3)
print(nums)

# 1. 크롤링 데이터에서 숫자만 추출
# 120mmHg -> 120

# 2. 단위 제거
# 170cm -> 170

# 3. 특정 형식 데이터 찾기
# 날짜 형식, 이메일 형식

# 4. 불필요한 특수 문자 제거