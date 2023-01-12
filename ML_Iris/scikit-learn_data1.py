'''
    * 머신러닝 분야의 고전적인 붓꽃(Iris) 데이터 셋
        0) 대표적인 지도 학습 데이터
        1) Setosa, Versicolor, Virginica 세 종류(품종)   -> y 즉 정답 / 레이블
            - Setosa : 부채붓꽃
            - Versicolor : 버시컬러
            - Virginica : 버지니카

        2) 입력 데이터는 4개의 특징을 가짐
            - sepal length(꽃받침 길이)
            - sepal width(꽃받침 너비)
            - petal length(꽃잎 길이)
            - petal width(꽃잎 너비)

        3) 150개의 꽃 샘플에서 꽃잎 길이와 꽃잎 너비    -> 독립변수

'''
from sklearn import datasets
import numpy as np


# 데이터 셋 불러오기
dataset = datasets.load_iris()


data = dataset["data"]
target = dataset["target"]
feature_names = dataset["feature_names"]

print(f"총 데이터 개수 : {len(data)}")
print(f"총 레이블 개수 : {len(target)}")
print("[출력 특징]")
for i in range(len(feature_names)):
    feature_name = feature_names[i]
    print(f"{i + 1} : {feature_name}")
print("입력 데이터 출력")
print(data[:5])


print("-" * 30)

target_names = dataset["target_names"]
print("[출력 특징]")
for i in range(len(target_names)):
    target_name = target_names[i]
    print(f"{ i + 1} : {target_name}")

print("입력 데이터 출력")
print(target[:5])

# #print(iris)
# X = iris.data[:, [2,3]]
# y = iris.target
#
# # iris.target에 저장된 세개의 고유한 클래스 레이블을 반환
# # 붓꽃 클래스 이름 : Iris-Setosa, Iris-Versicolor, Iris-Virginica 이미 정수로 저장되어 있음(0, 1, 2)
# print('클래스 레이블 : ', np.unique(y))   # 정답 = 레이블
#
# # 훈련된 모델 성능을 평가하기 위한 데이터셋을 훈련 데이터셋과 테스트 데이터셋으로 분할
# # 30%는 테스트 데이터, 70%는
# from sklearn.model_selection import train_test_split    # for 분할 / 7:3
#
#
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1, stratify=y)
# print('y의 레이블 카운트 : ', np.bincount(y))
# print('y_train의 레이블 카운트 : ', np.bincount(y_train))
# print('y_test의 레이블 카운트 : ', np.bincount(y_test))
#
#
