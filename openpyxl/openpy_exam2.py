from openpyxl import *

# == 시트 생성 ==
w2 = load_workbook('openpyxl/test.xlsx')

# 새로운 시트 하나 생성
new_ws = w2.create_sheet()

# 새로 만든 시트의 이름 설정
# 기본 이름 : Sheet1, Sheet2
new_ws.title = '마지막_시트'

# 변경사항 저장
w2.save('openpyxl/test.xlsx')