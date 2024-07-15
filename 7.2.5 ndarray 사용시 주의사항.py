import numpy as np

arr1 = np.array([1,2,3,4,5])
print(arr1)

arr2 = arr1
arr2[0] = 100

# arr2 변수를 변경하면 원래 변수(arr1)도 영향을 받음
print(arr1)

# ndarray를 copy()를 사용해 arr2 변수에 대입한 경우
arr1 = np.array([1,2,3,4,5])
print(arr1)

arr2 = arr1.copy()
arr2[0] = 100

print(arr1)
print(arr2)


