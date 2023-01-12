'''
    * 사이킷런 가상 데이터 생성
        1) 분류(classification) 모델 학습을 위한 가상 데이터 생성하기
        2) make_blobs
            - 정규 분포를 따르는 가상의 데이터 생성
            - 초승달 모양의 클러스터 두개 생성
            - 파라미터
                - n_samples : 생성할 데이터 개수 (default : 100)
                - noise : 데이터 노이즈 크기 / 0에 가까울수록 정확히 구분되는 두개의 초승달 형태를 띔
                    └> noise가 클수록 아웃라이어가 뚜렷하게 생성됨            
                - n_features : 입력 차원 (default : 2)
                - random_state : 랜덤 데이터 생성 시드 (seed)

'''
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons

X, y = make_moons(n_samples=500, noise=0.05, random_state=1234)
df = pd.DataFrame(dict(x=X[:, 0], y=X[:, 1], label=y))
print(df.head(10))


print("데이터 개수 : ", len(df))


plt.scatter(df["x"], df["y"], s=100, c=y)
plt.show()