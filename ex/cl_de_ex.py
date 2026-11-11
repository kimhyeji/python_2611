# 클로저(Closure) 데코레이터(Decorator)

# 클로저 : 내부 함수가 자신이 정의된 외부 함수의 변수들을 기억하고, 외부 함수의 실행이 끝난 후에도 해당 변수를 사용할 수 있는 구조

print('==== 1단계: 함수 안에 함수 만들기 ====')
def outer():
    print("outer 함수가 실행되었습니다.")

    def inner():
        print('inner 함수가 실행되었습니다.')

    return inner # 함수 자체를 반환
#   return inner() # 함수를 실행하고 그 결과를 반환

func = outer() 
func()

print('\n==== 2단계: 클로저 ====')
# 클로저는 '외부 함수의 변수를 기억하는 내부 함수'
def make_multiplier(x):
    # x는 make_multiplier 함수의 지역 변수

    def multiplier(n):
        # 내부 함수 multiplier는
        # 바깥 함수의 변수 x를 사용할 수 있다.
        return x * n

    return multiplier
    
times3 = make_multiplier(3)
print(times3(10))
print(times3(5))

print('\n==== 3단계: 데코레이터 기본 구조 ====')

# 데코레이터는 '함수를 꾸며주는 함수'
# 내부 구조는 클로저와 매우 유사

def decorator(func):
    # func는 꾸며줄 함수

    def wrapper():
        print('함수 실행 전')
        func()
        print('함수 실행 후')

    return wrapper

@decorator
def say_hello():
    print('안녕하세요')

say_hello()

print('\n==== 4단계: 매개변수가 있는 데코레이터 ====')

def decorator_width_args(func):
    def wrapper(name):
        print('실행 전')
        func(name)
        print('실행 후')
        
    return wrapper

@decorator_width_args
def say_name(name):
    print('이름 :', name)

say_name('홍길동')