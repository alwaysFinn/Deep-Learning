'''
    1. 파이썬 리스트 & 넘파이
        1) 넘파이 배열
            - 형상 (shape) : 차원의 크기를 지정하는 정수의 튜플
                - ex : (3, 3)
            - 축 (axis) : 차원
                - axis=1 (컬럼)
                - axis=0 (행)

            - shape: (3, )          <-- 1d 배열
                - 2 3 4
                    axis = 0 (행)

            - shape: (2, 3)         <-- 2d 배열
                - 2 3 4
                  6 7 8
                    axis = 0 (행)
                    axis = 1 (컬럼)

            - shape: (4, 3, 2)      <-- 3d 배열
                - 2 3 4
                  6 7 8
                  2 3 4
                  6 7 8
                        2 3 4
                        6 7 8
                        2 3 4
                        6 7 8

                axis = 0
                axis = 1
                axis = 2
        2) 넘파이의 핵심은 다차원 배열(ndarray) n dimension array
        3) 리스트와 넘파이의 가장 큰 차이는 계산 성능
            - 넘파이 : 대용량의 배열, 행렬 연산 수행 함수를 포함
        4) 파이썬의 리스트
                - 동일하지 않은 자료형을 가진 항목들을 담을 수 있음
                - 단순히 ㅇㅕ러 데이터가 나열된 것
           넘파이의 ndarray 객체
                - 동일한 자료형의 항목들만 저장함
                - 넘파이는 배열의 선형대수의 벡터 개념으로 다룸

        5) 넘파이의 강력한 배열 프로그래밍 기능이 넘파이가 인기있는 이유
            - 스칼라(scalar) 언어의 for문
                - 각 원소들을 순차적으로 처리해야 함
            - 데이터 병렬성(parallelism) 방식
                - 데이터를 잘게 쪼개어 각각에 대해 동일한 연산을 독립적으로 수행하는 방식
                - 그래픽 처리 장치(GPU)는 고성능 데이터 병렬 처리기로 현재 슈퍼컴퓨팅 차원으로 적극 활용됨
                - SIMD(single instruction multiple data) : 하나의 연산이 다수의 데이터에 동시에 적용되는 방식 (CPU)
                - 벡터화 연산
                    - 프로그래머가 효율적으로 고성능의 데이터 병렬 처리를 할 수 있게 해줌
                    - 계산 시간은 대략 20배 정도 단축됨

'''

import numpy as np

a = np.array([2,3,4])
print(a.shape)      # a 객체의 형상
print(a.ndim)       #         차원
print(a.dtype)      # 요소의 자료형
print(a.itemsize)   # 요소의 크기(byte)
print(a.size)       # 요소의 수

print()

store_a = [20, 10, 30]      # 파이썬 리스트   (매장 A의 매출)
store_b = [70, 90, 70]      # 파이썬 리스트   (매장 B의 매출)

# 월별 매출 합 구하기
list_sum = store_b + store_a
print(list_sum)
# 실행 결과 : [70, 90, 70, 20, 10, 30]
# 리스트는 값을 더하는 것이 아닌 리스트 끼리 합쳐지는 개념
# 따라서 월별 매출의 합을 구하려면 리스트끼리 합치는게 아닌 리스트의 각 행을 더해야 함

print()

# 넘파이 곱셈
arr1 = np.array([[1,2], [3,4], [5,6]])
arr2 = np.array([[2,2], [2,2], [2,2]])

result = arr1 * arr2
print(result)