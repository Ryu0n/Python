import numpy as np
import pandas as pd
import mglearn
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer

from IPython.display import display



# mglearn.plots.plot_knn_classification(n_neighbors=3)
# mglearn.plots.plot_knn_regression(n_neighbors=2)
# plt.show()


# kNN Classification - n_neighbors 개수의 이웃들 중에서 더 많이 속한 이웃의 클래스로 지정
def kNN_clf_forge():
    X, y = mglearn.datasets.make_forge()
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    knn_clf = KNeighborsClassifier(n_neighbors=3)

    # training
    knn_clf.fit(X_train, y_train)

    # prediction
    print(knn_clf.predict(X_test))

    # accuracy
    print(knn_clf.score(X_test, y_test))

def kNN_clf_breastCancer():
    cancer = load_breast_cancer()
    X_train, X_test, y_train, y_test = train_test_split(cancer['data'], cancer['target'], stratify=cancer['target'], random_state=66)

    training_accuracy = [] # 이웃의 수 별 학습 데이터 셋의 정확도
    test_accuracy = []     # 이웃의 수 별 테스트 데이터 셋의 정확도

    neighbors_settings = range(1, 11) # n_neighbors를 1부터 10까지 적용

    # 이웃의 수 별로 정확도를 파악하기 위함.
    for n_neighbor in neighbors_settings:
        knn_clf = KNeighborsClassifier(n_neighbors=n_neighbor)

        knn_clf.fit(X_train, y_train)

        training_accuracy.append(knn_clf.score(X_train, y_train))
        test_accuracy.append(knn_clf.score(X_test, y_test))

    plt.plot(neighbors_settings, training_accuracy, label='training accuracy')
    plt.plot(neighbors_settings, test_accuracy, label='test accuracy')
    plt.xlabel('n_neighbors'); plt.ylabel('accuracy');
    plt.legend() # 범례
    plt.show()

# kNN Regression - n_neighbors개의 이웃들의 평균값을 예측
def kNN_reg_wave():
    X, y = mglearn.datasets.make_wave(n_samples=40)
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    knn_reg = KNeighborsRegressor(n_neighbors=3)

    knn_reg.fit(X_train, y_train)

    print(knn_reg.predict(X_test))
    # R^2의 의미는 회귀에서의 적합도를 의미하며 1은 예측이 완벽한 경우, 0은 y_train의 평균으로만 예측하는 모델의 경우다. R^2는 음수가 될 수 있으며 이 경우는 예측값과 실제값이 상반된 경우다.
    # R^2 = 1 - (∑(y-prediction)^2 / ∑(y-mean(y))^2)
    print('test set R^2 : ', knn_reg.score(X_train, y_train))
    print('test set R^2 : ', knn_reg.score(X_test, y_test))


# kNN_clf_forge()
# kNN_clf_breastCancer()
kNN_reg_wave()
