'''
# 설치가 안될 시
import sys
# 파이썬이 설치된 경로 추출
print(sys.executable)
# 터미널 : 추출한 경로 -m pip install 외부라이브러리이름
'''

# openpyxl 불러오기 / 모든 기능을 불러옴
import openpyxl
# from openpyxl import *

# 버전 확인
print(openpyxl.__version__)