'''
    1. 텐서플로 일반적인 아키텍쳐
        1) 준비된 데이터를 사용하여 모델(모형)을 생성
            - 데이터 준비, 모델 정의, 모델 훈련, 모델 평가
        2) 생성된 모델을 사용하여 분류 및 예측
        3) 사용자에게 웹이나 모바일로 서비스를 배포 환경도 제공

    2. 텐서플로 2.x
        1) 기존 1.x 버전의 불편했던 문법 개선, tf.keras를 중심으로 high level API를 제공
        2) 텐서플로에서 딥러닝을 구현하는 순차적 방법으로 적용하면 됨

    3. 데이터 준비
        1) 데이터가 텍스트일 경우 (텍스트 모델을 사용해야 할 경우)
            - 서로 다른 길이의 시퀀스(sequence)를 분할하여 처리
'''
import os
import numpy as np  # 백터 및 행렬 연산에서 매우 편리한 기능 제공하는 파이썬 라이브러리 패키지
import tensorflow as tf
import pandas as pd # 데이터 분석을 위해 사용되는 파이썬 라이브러리 패키지
import matplotlib.pyplot as plt
import seaborn as sns

#로그레벨이 3 이 되면 warning이 뜨지 않음
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# 파일 실행
filename = os.listdir("ezen")[0]   #ezen 폴더 안에 첫번째꺼에 접근
file = open('ezen/' + filename, encoding='utf-8')   # 파일에 접근(by 순서, namespace)

'''
    * 데이터 셋을 열어보면 특성(컬럼) 일곱 개로 구성됨
        1) price : 자동차 가격
        2) maint : 자동차 유지 비용
        3) doors : 자동차 문 개수
        4) persons : 수용 인원
        5) capacity : 수하물 용량
        6) safety : 안전성
        7) output : 차 상태 / unacc(허용 불가), add(허용), good(양호), vgood(매우좋음)
  
'''

cols = ['price', 'maint', 'doors', 'persons', 'capacity', 'safety', 'output']  #csv 파일의 각 컬럼에 대한 정의
cars = pd.read_csv(file, names=cols, header=None)
print(cars)
print('-------------------------------------------------------------------')

'''
    * 데이터에 대한 전처리
        1) 딥러닝은 통계 알고리즘 기반으로 하기 때문에 범주 정보를 숫자로 변환해야 함
        2) 원 - 핫 인코딩 (one-hot encoding) 기법 사용
            - 새로운 열을 생성
            - 고유값을 갖는 경우 1값 부여 
        3) get_dummies()
            - 가변수(dummy variable)를 만들어 주는 함수
            - 문자를 숫자(0, 1) 로 바꿔주는 것
        4) concat() : 여섯개 열 병합(문자열로 결합)
'''
price = pd.get_dummies(cars.price, prefix='price')
maint = pd.get_dummies(cars.maint, prefix='maint')
doors = pd.get_dummies(cars.doors, prefix='doors')
persons = pd.get_dummies(cars.persons, prefix='persons')
capacity = pd.get_dummies(cars.capacity, prefix='capacity')
safety = pd.get_dummies(cars.safety, prefix='safety')

labels = pd.get_dummies(cars.output, prefix='output')   # 정답에 해당

X = pd.concat([price, maint, doors, persons, capacity, safety], axis=1)
y = labels.values

print(X)
print(y)

'''
    * 모델 정의
        1) Sequential API
            - 다차원 입출력을 갖는 신경망 구현
            - 텐서플로 2에서 케라스를 이용
            - 케라스는 텐서플로 런타임을 이용해서 동작
                
'''
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)  # 전처리 즉, 준비과정

# keras 사용, 모델 정의