import numpy as np

X = np.array([
    [0, 1, 0, 1],
    [1, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 1, 0]
])

y = np.array([0, 1, 0, 1])

counts = {}
for label in np.unique(y):
    print(y == label) # [ True False  True False], [False  True False  True]
    print(X[y == label]) # [[0 1 0 1] [0 0 0 1]], [[1 0 1 1] [1 0 1 0]]
    counts[label] = X[y == label].sum(axis=0) # axis=0 은 열을 의미. 즉, 클래스가 0인 데이터 포인트 [0, 1, 0, 1] 과 [0, 0, 0, 1]에서 각 특성별로 0읜 것들의 합을 구함.
print(counts)