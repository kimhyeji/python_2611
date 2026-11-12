import numpy as np

'''
Numpy : 파이썬에서 수학과 데이터 분석을 쉽게 할 수 있도록 도와주는 라이브러리
ndArray : 숫자를 여러 차원으로 저장할 수 있는 배열
Numpy로 할 수 있는 것들
    - 숫자 묶음 생성
    - 평균, 합계, 최댓값
    - 배열
    - 2차원 표(행렬)
'''


print('===== 일반 리스트 =====')
a = [1, 2, 3]
b = [4, 5, 6]

print(a + b)


print('===== numpy 01 =====')
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
# np.array([]) => 리스트 처럼 보이지만 실제로는 수학용 배열. 모든 원소가 같은 타입
print(a + b)


print('===== numpy 02 =====')
# 1차원 ndArray 생성(숫자 4개가 한 줄로 있는 배열)
np.array([1, 2, 3, 4])

arr1 = np.array([1, 2, 3, 4]) # numpy 배열임을 알려줌
arr2 = [1, 2, 3, 4] # 일반 리스트

# <class 'numpy.ndarray'>
# 넘파이로 이루어진 다차원 배열
print(type(arr1))

# <class 'list'>
# 파이썬 리스트 형태
print(type(arr2))


print('===== numpy 03 =====')
# 1차원 배열 : 숫자가 한 줄로 늘어선 형태
# 2차원 배열 : 숫자가 가로와 세로로 된 표 모양
# 3차원 배열 : 2차원 배열이 여러 장 겹친 입체 모양

# 2차원 ndArray 생성
# 1차원 배열 두개가 리스트로 묶인 형태
arr2 = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8]])

arr3 = np.array([[[1, 2, 3, 4], [1, 2, 3, 4]],
                [[1, 2, 3, 4], [1, 2, 3, 4]]])

print('2차원 배열 arr2')
print(arr2)

print('3차원 배열 arr3')
print(arr3)


print('===== numpy 04 =====')
a = np.array([1, 2, 3, 4])

print(a + 1)
print(a * 2)
print(a ** 2)
# for문을 안 쓰고도 계산이 가능


print('===== numpy 05 =====')
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8]])
arr3 = np.array([[[0.1, 0.2, 0.3, 0.4], [5, 6, 7, 8]],
                [[1, 2, 3, 4], [1, 2, 3, 4]]])

# ndim : 배열의 차원 수
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)

# shape : 배열의 형태(배열 구조를 튜플로 보여줌)
# 튜플 : 리스트와 비슷하지만 가장 큰 차이점은 한 번 생성한 튜플의 요소를 수정하거나 삭제할 수 없다
# (총 개수, 행 개수, 열 개수)
print(arr1.shape) # (4, ) = 4
print(arr2.shape) # (2, 4) = 8
print(arr3.shape) # (2, 2, 4) = 16

# size : 배열 요소의 총 개수
print(arr1.size) # 4
print(arr2.size) # 8
print(arr3.size) # 16

# dtype : 배열 요소의 데이터 타입
print(arr1.dtype)
print(arr2.dtype)
print(arr3.dtype)

# itemsize : 배열 원소 하나가 차지하는 메모리 크기
print(arr1.itemsize)
print(arr2.itemsize)
print(arr3.itemsize)

# data : 배열의 실제 데이터가 저장된 메모리 버퍼(buffer 주소)
print(arr1.data)
print(arr2.data)
print(arr3.data)


print('===== numpy 06 =====')
# ndArray T : 전치 행렬(행/열을 서로 바꾸는 것)
arr = np.array([[1, 2, 3], 
                [4, 5, 6]])

print('원래 배열')
print(arr)

print('전치 배열')
print(arr.T)


print('===== numpy 07 =====')
# ndArray.flatten() : 1차원으로 펼치기
arr = np.array([[1, 2, 3], 
                [4, 5, 6]])

print('원래 배열')
print(arr)

print('1차원으로 펼친 배열')
print(arr.flatten())

# flatten()은 복사본(copy)을 만든다
flat = arr.flatten()
flat[0] = 100

print('배열 출력')
print(arr)
print(flat)