# file : ds04_orderedList.py
# desc : 선형리스트 프로그램

kakaotalk = [] # 빈 배열 생성

# 데이터 추가함수
def add_data(friend):
    kakaotalk.append(None) # 배열 빈자리를 생성
    size = len(kakaotalk) # 배열의 전체 크기를 확인
    kakaotalk[size - 1] = friend

# 데이터 삽입함수
def insert_data(pos, friend):
    if pos < 0 or pos > len(kakaotalk):
        print('데이터 삽입범위 초과')
        return # 험수를 빠져나감
    
    # 정상적인 처리 시작
    kakaotalk.append(None) # 빈칸추가
    size = len(kakaotalk) # 배열의 현재크기
    # 삽입위치까지 데이터를 하나씩 뒤로 보냄
    for i in range(size-1, pos, -1): # 역순으로 맨뒤에서부터
        kakaotalk[i] = kakaotalk[i-1]
        kakaotalk[i-1] = None

    kakaotalk[pos] = friend

## 데이터 삭제함수
def delete_data(pos): # 데이터 삭제시는 위치값만
    if pos < 0 or pos >= len(kakaotalk):
        print('데이터 삭제범위 초과')
        return
    
    size = len(kakaotalk)
    kakaotalk[pos] = None # 데이터 삭제

    for i in range(pos+1, size):
        kakaotalk[i - 1] = kakaotalk[i] # 뒤에 값을 앞으로
        kakaotalk[i] = None
        
    del(kakaotalk[size-1]) # 배열의 맨 마지막 값 삭제

# 전역변수 선언
kakaotalk = []
select = -1 # 1/추가 2/삽입 3/삭제 4/종료

if __name__ == '__main__':
    while (select !=4):
        select = int(input('선택(1:추가, 2:삽입, 3:삭제, 4:종료) > '))

        if select == 1:
            data = input('추가 데이터 --> ')
            add_data(data)
            print(kakaotalk)
        elif select ==2:
            pos = int(input('삽입 위치 --> '))
            data = input('추가 데이터 --> ')
            insert_data(pos, data)
            print(kakaotalk)
        elif select ==3:
            pos = int(input('삽입 위치 --> '))
            delete_data(pos, data)
            print(kakaotalk)
        elif select ==4:
            exit(0) # 프로그램 완전 종료 함수
        else:
            print('1~4 중 하나를 입력하세요')
            continue
            