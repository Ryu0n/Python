import numpy as np

# arange
a = np.arange(0, 10, step=5) # [0 5]
b = np.arange(1, 10, 5)      # [1 6]
c = np.arange(0, 10, step=1) # [0 1 2 3 4 5 6 7 8 9]
d = np.arange(10, 3, -2)     # [10  8  6  4]

print(a); print(b); print(c); print(d)

# linspace - num : 간격 갯수, endpoint : 마지막 값 표함 여부, retsetp : 간격 포함 여부
a = np.linspace(0, 10, num=5, endpoint=True, retstep=True) # (array([ 0. ,  2.5,  5. ,  7.5, 10. ]), 2.5)
b = np.linspace(0, 10, num=5, endpoint=True, retstep=False) # [ 0.   2.5  5.   7.5 10. ]
c = np.linspace(0, 10, num=5, endpoint=False, retstep=False) # [0. 2. 4. 6. 8.]

print(a); print(b); print(c);

# logspace - base : 로그 값의 간격
a = np.logspace(0, 10, num=5, endpoint=True, base=10.0)