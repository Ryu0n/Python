import numpy as np
import pandas as pd
import mglearn
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso

from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC

from sklearn.model_selection import train_test_split

from sklearn.datasets import load_breast_cancer
from sklearn.datasets import make_blobs

from IPython.display import display

# mglearn.plots.plot_linear_regression_wave()
# plt.show()

def linear_reg_wave():
    X, y = mglearn.datasets.make_wave(n_samples=60)
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

    lr = LinearRegression().fit(X_train, y_train)

    print('lr.coef_ : ', lr.coef_)           # 가중치가 저장되어 있음.
    print('lr.intercept_ : ', lr.intercept_) # 절편이 저장되어 있음.

    print('training set score : ', lr.score(X_train, y_train))
    print('test set score : ', lr.score(X_test, y_test))
    # 트레이닝 셋 점수와 테스트 셋 점수가 비슷하면 과소 적합 (Underfitting)
    # 1차원 데이터 셋에서는 Overfiting을 걱정할 필요가 없다.

def linear_reg_boston():
    X, y = mglearn.datasets.load_extended_boston()
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    lr = LinearRegression().fit(X_train, y_train)
    print('\nLinear Regression')
    print('training set score : ', lr.score(X_train, y_train))
    print('test set score : ', lr.score(X_test, y_test))
    # 다음과 같이 트레이닝 셋의 점수는 높은데 테스트 셋의 점수가 낮으면 Overfitting
    # Overfitting을 방지하기 위해 정규화가 포함된 regression을 수행한다. (Ridge, Lasso) - 모델의 복잡도를 제어할 수 있어야함.

# Ridge Regression - Liear Regression + L1 normalization
def ridge_reg_boston(alpha):
    X, y = mglearn.datasets.load_extended_boston()
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    ridge = Ridge(alpha=alpha).fit(X_train, y_train)

    print('\nRidge Regression')
    print('training set score : ', ridge.score(X_train, y_train))
    print('test set score : ', ridge.score(X_test, y_test))

# Lasso Regression - Linear Regression + L2 normalization
def lasso_reg_boston(alpha):
    X, y = mglearn.datasets.load_extended_boston()
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    lasso = Lasso(alpha=alpha).fit(X_train, y_train)

    print('\nLasso Regression')
    print('training set score : ', lasso.score(X_train, y_train))
    print('test set score : ', lasso.score(X_test, y_test))
    print('feature using : ', np.sum(lasso.coef_ != 0)) # L1 normalization으로 인해 0이 되지 않은 특성들의 갯수 (사용중인 특성의 갯수)

# Linear Classification - Logistic Regression, Linear SVC (선형 서포트 벡터 분류기)
def linear_clf_forge():
    X, y = mglearn.datasets.make_forge()

    fig, axes = plt.subplots(1, 2, figsize=(10, 3))

    for model, ax in zip([LinearSVC(), LogisticRegression()], axes):
        clf = model.fit(X=X, y=y)
        mglearn.plots.plot_2d_separator(clf, X, fill=False, eps=0.5, ax=ax, alpha=.7)
        mglearn.discrete_scatter(X[:, 0], X[:, 1], y, ax=ax)
        ax.set_title(clf.__class__.__name__)
        ax.set_xlabel("feature 0")
        ax.set_ylabel("feature 1")
    axes[0].legend()
    plt.show()

    mglearn.plots.plot_linear_svc_regularization()
    plt.show()

# C값은 규제 강도와 반비례 : C가 클수록 규제 강도가 떨어져서 overfitting
def logistic_reg_breast_cancer(C):
    cancer = load_breast_cancer()
    X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, stratify=cancer.target, random_state=42)
    logistic_reg = LogisticRegression(C=C).fit(X_train, y_train)
    print('train set score : ', logistic_reg.score(X_train, y_train))
    print('test set score : ', logistic_reg.score(X_test, y_test))

def linear_SVC_blobs():
    X, y = make_blobs(random_state=42)

    mglearn.discrete_scatter(X[:, 0], X[:, 1], y) # 특성1과 특성2와 라벨(클래스는 3개 - 0, 1, 2)
    plt.xlabel('feature 0')
    plt.ylabel('feature 1')
    plt.legend(['class0, class1, class2'])
    plt.show()

    linear_svc = LinearSVC().fit(X, y)
    print('number of weights : ', linear_svc.coef_.shape) # (3, 2) : 3개의 클래스에 각각 2개의 특성이 반영되어 있으므로 각각의 선형 모델별 특성들에 대한 가중치
    print(linear_svc.coef_)

    print('number of biases : ', linear_svc.intercept_.shape) # (3,) : 각각의 선형 모델들의 절편
    print(linear_svc.intercept_)

# linear_reg_wave()
# linear_reg_boston()
# ridge_reg_boston(0.1)
# lasso_reg_boston(0.01)
# linear_clf_forge()
# logistic_reg_breast_cancer(1.0)
linear_SVC_blobs()