'''
    1. 파이썬 예외 처리
        1) 예외 (exception) : 코드 실행 도중 발생하는 오류(error)

        2) try:
            기본적으로 실행할 코드
           except:
            예외 발생 시 실행할 코드

'''
try:
    x = 10
    result = x/0
    print(result)
except:       # 각 예외 케이스 명시가 정석 except(ZeroDivisionError)
    print("예외 발생")

print("================================================")

arr = [7, 5, 3]
index = 4

try:
    data = arr[index]
except IndexError as e:
    print("IndexError 발생")
    print(e)

print()

data_list = [1,2,3,4,5]
index = 3
x = 0

try:
    data = data_list[index]
    result = data / x
    print(result)
except IndexError as e:
    print("배열 범위 넘어서 발생한 에러")
    print(e)
except ZeroDivisionError as z:
    print("0으로 나눠서 발생한 에러")
    print(z)