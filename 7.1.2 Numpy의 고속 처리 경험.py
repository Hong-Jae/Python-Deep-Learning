import numpy as np
import time
from numpy.random import rand

N = 150

matA = np.array(rand(N, N))
matB = np.array(rand(N, N))
matC = np.zeros((N, N), dtype=float)  # float형으로 초기화

start = time.time()

for i in range(N):
    for j in range(N):
        for k in range(N):
            matC[i][j] += matA[i][k] * matB[k][j]  # += 연산자로 변경

print("파이썬 기능만으로 계산한 결과: %.2f[sec]" % float(time.time() - start))
print("matC (파이썬 기능으로 계산한 결과):")
print(matC[:5, :5])  # 행렬의 일부만 출력

start = time.time()

matC = np.dot(matA, matB)

print("NumPy를 사용하여 계산한 결과: %.2f[sec]" % float(time.time() - start))
print("matC (NumPy로 계산한 결과):")
print(matC[:5, :5])  # 행렬의 일부만 출력




# import numpy as np
# import time
# from numpy.random import rand
# N = 150

# matA = np.array(rand(N,N))
# matB = np.array(rand(N,N))
# matC = np.array([[0] * N for _ in range(N)])

# start = time.time()

# for i in range(N):
#   for j in range(N):
#     for k in range(N):
#       matC[i][j] = matA[i][k] * matB[k][j]


# print("파이썬 기능만으로 계산한 결과: %.2f[sec]" % float(time.time() - start))

# start = time.time()

# matC = np.dot(matA, matB)

# print("NumPy를 사용하여 계산한 결과: %.2f[sec]" % float(time.time() - start))
