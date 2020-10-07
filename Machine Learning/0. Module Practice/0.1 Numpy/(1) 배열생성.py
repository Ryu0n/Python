import numpy as np

# numpy는 벡터 행렬 계산을 효율적으로 처리하기 위한 모듈

# 1. 배열 생성
a = [1, 2, 3, 4, 5]
b = np.array(a)
c = np.array([1, 3, 5])


d = b        # 같은 객체 ([1 2 3 4 5])를  b와 d 가르킨다. 즉, 둘중 하나라도 수정하면 상대방에게도 영향이 간다.
e = b.copy() # 별도의 객체를 복사하여 e가 가르킨다. 즉, 독립적.

print(a, b, c) # [1, 2, 3, 4, 5] [1 2 3 4 5] [1 3 5]
print(d, e) # [1 2 3 4 5] [1 2 3 4 5]

b[0] = 6
print(d) # [6 2 3 4 5] : d를 수정해도 b에 반영된다. 같은 객체를 가르키기 때문이다.

# 2. 배열 호출 (인덱싱 및 슬라이싱)
print(b[2]) # 3
print(c[-1]) # 5
print(c[1:3]) # [3 5]

# 3. 배열 계산
print(a*2) # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5] : list에서는 * 연산을 사용하면 같은 값이 n번 반복된다.
print(b*2) # 반면 numpy 배열에서는 각 원소들이 2씩 곱해진다.
# print(a+3) # list 타입에서는 지원하지 않는 연산
print(c+3) # 각 원소들에 3이 더해진다.
# 정리하자면 numpy 배열에 연산자를 사용하면 배열의 각 원소에 broad casting을 하게 된다.

# 4. 1차원 배일
a = np.array([1, 2, 3], dtype=int)
b = np.array([1.1, 2.2, 3.3], dtype=float)
c = np.array([1, 1, 0], dtype=bool)

# 5. 다차원 배열
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])

# 6. 배열 속성 반환
print('a.ndim : ', a.ndim) # a.ndim :  2
print('a.shape : ', a.shape) # a.shape :  (3, 3)
print('a.dtype : ', a.dtype) # a.dtype :  int32

print('np.ndim : ', np.ndim(b)) # np.ndim :  3
print('np.shape : ', np.shape(b)) # np.shape :  (3, 2, 2)

# ndim : 배열의 차원 반환
# shape : 배열의 형태 반환
# dtype : 배열의 자료형

# 7. 모든 값이 1인 배열
a = np.ones((2, 2), dtype=int) # [[1 1] [1 1]]
b = [1, 2, 3, 4, 5]
c = np.ones_like(b, dtype=int) # [1 1 1 1 1] shape는 인자와 동일

print(a, b, c)

# 8. 모든 값이 0인 배열
a = np.zeros((2, 2), dtype=int) # [[0 0] [0 0]]
b = [1, 2, 3, 4, 5]
c = np.zeros_like(b, dtype=int) # [0 0 0 0 0]

print(a, b, c)

# 9. 모든 값이 비어있는 배열
d = np.empty((2, 2), dtype=int)
e = [1, 2, 3, 4, 5]
f = np.empty_like(b, dtype=int)

print(d, e, f)

# 10. 대각의 값이 1인 배열 (단위 행렬)
a = np.identity(4, dtype=int)
# [[1 0 0 0]
#  [0 1 0 0]
#  [0 0 1 0]
#  [0 0 0 1]]
b = np.eye(4, 4, k=1, dtype=int)
# [[0 1 0 0]
#  [0 0 1 0]
#  [0 0 0 1]
#  [0 0 0 0]]
c = np.eye(4, 4, k=-1, dtype=int)
# [[0 0 0 0]
#  [1 0 0 0]
#  [0 1 0 0]
#  [0 0 1 0]]
d = np.eye(4, 4, dtype=int)
# [[1 0 0 0]
#  [0 1 0 0]
#  [0 0 1 0]
#  [0 0 0 1]]

print(a)
print(b)
print(c)
print(d)