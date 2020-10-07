import pandas as pd
import mglearn
import matplotlib.pyplot as plt

from IPython.display import display
from pandas.plotting import scatter_matrix
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris_dataset = load_iris()

# print(type(iris_dataset))
print(iris_dataset.keys())
# print(iris_dataset['DESCR'])
print(iris_dataset['target_names'])  # 3 classes
print(iris_dataset['feature_names']) # 4 features

# data
print(type(iris_dataset['data']))
print(iris_dataset['data'].shape) # (150, 4) : 4 features, 50 datas in each class

# label
print(type(iris_dataset['target']))
print(iris_dataset['target'].shape) # (150,) : labels in each data

# train set (75% : X_train : 학습 데이터, y_train : 학습 라벨), test set (25% : X_test : 테스트 데이터, y_test : 테스트 라벨)를 적절히 분리하기 위함.
X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state=0)

print(X_train.shape, y_train.shape) # 75% : 112개
print(X_test.shape, y_test.shape)   # 25% :  38개

# 데이터들이 머신러닝에 적합한지 판단하기 위해 산점도(scatter plot)를 활용하여 확인해 볼 필요가 있다.
# 먼저 numpy array를 pandas DataFrame으로 바꿔야 한다. (pandas에서 scatter_matrix() 함수를 지원하기 때문)
iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset['feature_names'])
display(iris_dataframe)
pd.plotting.scatter_matrix(iris_dataframe, c=y_train, figsize=(15, 15), marker='o', hist_kwds={'bins':20}, s=60, alpha=.8, cmap=mglearn.cm3)
plt.show()

# k-Nearest Neighbors classifier
from sklearn.neighbors import KNeighborsClassifier
kNN = KNeighborsClassifier(n_neighbors=1) # 훈련 데이터에 근접한(빈도수가 높음) k(1)개의 이웃(클래스)를 찾음.
kNN.fit(X_train, y_train) # fit 메소드는 knn객체 자체를 학습된 모델 형태로 반환(변경)한다.

# k-Nearest Neighbors classifier prediction
import numpy as np
X_new = np.array([[5, 2.9, 1, 0.2]]) # shape : (1, 4) - 1 data, 4 features
prediction = kNN.predict(X_new)
print(iris_dataset['target_names'][prediction])

# k-Nearest Neighbors classifier evaluation
y_preds = kNN.predict(X_test)

for y_pred in y_preds:
    print(iris_dataset['target_names'][y_pred])

print(np.mean(y_preds == y_test)) # 예측값과 실제라벨의 일치성 평균 (정확도)
print(kNN.score(X_test, y_test)) # kNN객체의 score 메소드로도 정확도 계산 가능