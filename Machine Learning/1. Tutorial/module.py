import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mglearn

from scipy import sparse
from IPython.display import display



# numpy
x = np.array([[1, 2, 3], [4, 5, 6]])
print(x, '\n')

eye = np.eye(4)
print(eye, '\n')

# scipy
# 희소행렬 생성 - 0을 전부 저장하면 메모리 부족이 발생할 수 있으므로
sparse_matrix = sparse.csr_matrix(eye)
print(sparse_matrix, '\n')
# 희소행렬 생성 - COO format
data = np.ones(4)
row_indices = np.arange(4); col_indices = np.arange(4);
eye_coo = sparse.coo_matrix((data, (row_indices, col_indices)))
print(eye_coo, '\n')

# matplot
x = np.linspace(-10, 10, 100) # -10부터 10까지 100개의 간겨으로 나누어진 배열
y = np.sin(x)
print(x, y)
plt.plot(x, y, marker="x")
plt.show()

# pandas
data = {'Name':["John", "Anna"],
        'Location':["New York", "Paris"],
        'Age':[24, 13]}
data_pandas = pd.DataFrame(data)
display(data_pandas)
display(data_pandas[data_pandas.Age > 13])
# print(data_pandas, '\n')
# print(data_pandas[data_pandas.Age > 13]) # 테이블에 쿼리 날리는 법
