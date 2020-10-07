import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mglearn

from sklearn.datasets import load_breast_cancer

from sklearn.tree import export_graphviz # 트리  .dot 파일 생성
import graphviz # .dot 파일을 읽기 위함

from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor

from sklearn.model_selection import train_test_split

def DT_clf_breast_cancer(depth):
    cancer = load_breast_cancer()
    X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, stratify=cancer.target, random_state=42)
    # max_depth 에 대한 옵션을 주지 않으면 무한정으로 순수 노드로 분류될 때까지 트리의 깊이가 깊어져 과대적합 또는 일반화가 잘 되지 않는다.
    tree = DecisionTreeClassifier(max_depth=depth, random_state=0)
    tree.fit(X_train, y_train)
    print('training set score : ', tree.score(X_train, y_train))
    print('test set score : ', tree.score(X_test, y_test))

    # malignant : 악성 / benign : 양성
    export_graphviz(tree, "tree.dot", class_names=['malignant', 'benign'], feature_names=cancer.feature_names, impurity=False, filled=True)
    with open("tree.dot", encoding='utf-8') as f:
        dot_graph = f.read()
    dot = graphviz.Source(dot_graph); dot.format = 'png'; dot.render(filename='tree')

    # feature importance(특성 중요도) - 각 특성별로 얼마나 중요한지 평가함.
    # 각 특성에 대해 1인 경우는 완벽하게 타깃 클래스를 예측 , 0인 경우는 사용되지 않음.
    # 모든 특성 중요도의 합은 1이다.
    print(tree.feature_importances_)

    return tree

def plot_feature_importances_cancer(model):
    cancer = load_breast_cancer()
    n_features = cancer.data.shape[1]

    plt.barh(np.arange(n_features), model.feature_importances_, align='center')
    plt.yticks(np.arange(n_features), cancer.feature_names)
    plt.xlabel('feature importance')
    plt.ylabel('feature')
    plt.ylim(-1, n_features);
    plt.show()

# tree = DT_clf_breast_cancer(4)
# plot_feature_importances_cancer(tree)

# tree = mglearn.plots.plot_tree_not_monotone()
# plt.show(tree)

ram_prices = pd.read_csv(os.path.join(mglearn.datasets.DATA_PATH, "ram_price.csv"))

print(ram_prices)


# 로그 스케일이란? 10^n 단위를 의미. 기하급수적으로 커지는 데이터에 대하여 일정한 간겨으로 보기 위함.
# semilogx : x축 데이터에 대하여 로그 스케일 적용
# semilogy : y축 데이터에 대하여 로그 스케일 적용
plt.yticks(fontname="Arial")
plt.semilogy(ram_prices.date, ram_prices.price) # 인자 : x축 데이터, y축 데이터
plt.xlabel("year"); plt.ylabel("price");
plt.show()

# plt.semilogx(ram_prices.price, ram_prices.date)
# plt.ylabel("year"); plt.xlabel("price");
# plt.show()

data_train = ram_prices[ram_prices.date < 2000]
data_test = ram_prices[ram_prices.date >= 2000]

X_train = data_train.date[:, np.newaxis]
y_train = np.log(data_train.price)

tree = DecisionTreeRegressor().fit(X_train, y_train) # 2000년도 전까지의 데이터를 학습

X_all = ram_prices.date[:, np.newaxis] # 전체 기간에 대한 예측 그러나, 트리의 단점은 학습한 데이터의 범위를 벗어나면 새로운 예측이 불가능하다.

pred_tree = tree.predict(X_all)
price_tree = np.exp(pred_tree)

plt.semilogy(data_train.date, data_train.price, label='training data')
plt.semilogy(data_test.date, data_test.price, label='test data')

plt.semilogy(ram_prices.date, price_tree, label='tree predict')

plt.legend(); plt.show()