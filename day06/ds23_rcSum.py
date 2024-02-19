# file : ds23_rcSum.py
# desc : 재귀호출 합산함수

def addNumber(num):
    if num <=1:
        return 1
    
    return num + addNumber(num-1)

sum = addNumber(5)
print(sum)