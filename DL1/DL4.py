'''
    1. 인공지능 : 인간처럼 학습하고 추론하는 프로그램 연구
       머신러닝 : 인공지능의 한분야, 스스로 학습하는 프로그램 연구
                    - 통계학과 달리 보통 대량의 복잡한 데이터셋을 다루므로 전통적인 통계분석 방법은 현식적으로 적용하기 힘듦
                    - 특히 딥러닝은 수학적 이론이 비교적 부족, 근복적으로 엔지니어링 분야에 해당
                    - 경험적 발견에 의해 주도되는 실천적인 분야, 소프트웨어 및 하드웨어 발전에 크게 의존

       딥 러닝 : 인공신경망 사용하여 빅데이터로부터 학습하는 프로그램 연구
       1) 신경망 (neural network)은 1950년대부터 연구됨
            - 딥러닝의 기원은 인공 신경망
                - 뇌에 수많은 뉴런(신경)이 존재, 시냅스로 서로 연결되어 있는데, 이를 신경망(neural network)라고 함
       2) 최근의 인공지능 붐은 전적으로 딥러닝의 성공 덕
       3) 많은 레이어(layer)가 있는 신경 회로망을 사용하여 데이터의 추상화를 모델링하는 기계학습의 한 분야


    2. 인공지능 역사
        1) 탐색의 시대
        2) 지식의 시대
        3) 학습의 시대
            - AI의 부활
            - 자율 주행 자동차
            - 광고 (추천 시스템)
            - 챗봇
            - 의료분야, 진단
            - 언어 번역 (자연어 처리)
            - 경영 분야 (빅데이터 -> 인공지능 -> 경영의사 결정)
            - 딥러닝 예술 (화풍 모방)
            - 음악

    3. 신경망
            1) 인공 신경망(Artificial neural network: ANN)
                - 생물학적인 신경망에서 영감을 받아 만들어진 컴퓨터 구조
                    - 인간의 뇌 구조 모방
                - 장점
                    - 학습이 가능함 (데이터가 주어지면 신경망은 배울 수 있음)
                    - 몇 개의 소자가 오작동하더라도 전체적으로 큰 문제 발생 X


    4. 퍼셉트론(perceptron)
        1) 생물학적 뉴런 모방하여 만든 인공신경망의 기본 단위
            - 이전 perceptron과 연결  -->    inputs           weights     input function       activation function    -->    다음 perceptron과 연결
            - 입력 ----> 모두 더함 ----> 함수 ----> 출력
                w
            - 딥러닝은 가중치(Wn)을 수정하는 행위
            - 뇌세포는 항상 일정한 크기의 값을 출력함 (0 or 1)
            - 뇌세포의 출력물은 디지털 신호로 간주 가능

        2) activation function (활성화 함수 )
            - 입력 신호(x1, x2)의 가중치의 합이 어떤 임계값을 넘는 경우에만 뉴런이 활성화되어 1을 출력(y),
              그렇지 않으면 0을 출력함
            - if(w1x1 + w2x2 + b >= 1) ==> 1
                otherwise ==> 0
            - 계단(step) 함수
                - 시그모이드 함수 : 가장 무난한 형태로 널리 활용됨
                - 하이퍼블릭 탄잰트 함수 : 최근 음수값을 사용하지 않으려는 추세로 선호도 낮아짐
                - 렐루 함수 : 딥러닝 성능을 크게 향상시키는 경향이 있어 널리 활용됨
                - 리키 렐루 함수 : 음수값 정보가 일부 보정되어 렐루보다 성능이 뛰어남

                - 출력값 계산 예
                    - 입력값 = (1, 2, 3, 4, 5)
                    - 가중치 = (0.1, 0.2, 0.5, 0.6, 0.1)
                    - 가중치 적용된 입력값
                            = (1*0.1 + 2*0.2 + 3*0.5 + 4*0.6 + 5*0.1)
                    - 출력값 = 4.9
        3) 논리 연산을 하는 퍼셉트론

            x1              x2              y(X1 AND X2)        y(X1 or X2)         y(X1 XOR X2)
            0               0               0                        0                    0
            0               1               0                        1                    1
            1               0               0                        1                    1
            1               1               1                        1                    0
    4) AND / OR 연산
        - 초기 퍼셉트론을 이용, 문제해결은 AND와 OR 같은 간단 연산이었음
            - 기계가 AND와 OR 연산을 스스로 풀 수 있으면 이를 조합해 어떤 문제든 풀어낼 수 있다고 생각했음
        - 각 표본의 입력에 대한 출력값을 X-Y 평면 표시
        - 서로 다른 두 그룹을 구분하기 위해 선형 분류자 1개 필요
            - 퍼셉트론을 통한 선형 분리가 가능한 것을 확인

    5) XOR 연산
        - 하나의 선형 분류자로 두 그룹을 분류 불가
        - 기존의 퍼셉트론으로는 XOR 연산이 절대 불가능하다는 가설을 수학적으로 증명(1969년)
        - 퍼셉트론을 여러개 쌓아 올린 다층 퍼셉트론(MLP, Multi Layer Perceptron)을 통해 XOR 연산에 대한 문제 해결
        - 각각의 가중치(Weight)와 편향(Bias)을 학습시킬 방법의 한계 언급 ==> 침체기 직결
'''
import numpy as np

epsilon = 0.0000001         # 부동소수점 오차를 방지하기 위함

def perceptron(x1, x2):
    w1, w2, b = 1.0, 1.0, -1.5
    sum_ = w1 * x1 + w2 * x2 + b
    if sum_ > epsilon:
        return 1
    else:
        return 0

print(perceptron(0, 0))
print(perceptron(0, 1))
print(perceptron(1, 0))
print(perceptron(1, 1))