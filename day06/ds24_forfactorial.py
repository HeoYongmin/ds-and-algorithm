# file : ds24_forfactoial.py
# desc : 반복문으로 팩토리얼 구하기
# n! = 1x2x3x......x(n-1)xn

n= 20
factValue = 1 # 곰셉이므로 1부터

for i in range(10, 0, -1): # 10부터 1까지 역순으로
    factValue *=i

print(f'{n}! = {factValue}')

# 재귀호출 factorial
def factorial(num):
    if num <=1: return 1

    return num * factorial(num-1)

print(f'{n}! = {factorial(n)}')
# 10 = 3628800, 20 =