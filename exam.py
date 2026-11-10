'''
class Person():
    def __init__(self, name, age, hobby):
        self.hello = "안녕하세요"
        self.name = name
        self.age = age
        self.hobby = hobby

jin = Person('진', 22, '운동')
'''

# 클래스 속성
class Person:
    __weight = 80
    folder = [] # 클래스 속성(공용)

    def add_files(self, file):
        self.folder.append(file)

    def print_weight(self):
        print(Person.__weight)

jin = Person()
jin.print_weight()
jin.add_files('txt')

kim = Person()
kim.add_files('img')

print(jin.folder)
print(kim.folder)