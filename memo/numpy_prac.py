import numpy as np

a = np.array([[1, 2], [3, 4], [5, 6]])

# 정수 배열 인덱싱의 예.
# 반환되는 배열의 shape는 (3,)
print(a[[0, 1, 2]])
print(a[[0, 1, 2], [0, 1, 0]])
print(a.shape)
# 출력 "[1 4 5]"
#
# # 위에서 본 정수 배열 인덱싱 예제는 다음과 동일합니다:
# print np.array([a[0, 0], a[1, 1], a[2, 0]])  # 출력 "[1 4 5]"
#
# # 정수 배열 인덱싱을 사용할 때,
# # 원본 배열의 같은 요소를 재사용할 수 있습니다:
# print a[[0, 0], [1, 1]]  # 출력 "[2 2]"
#
# # 위 예제는 다음과 동일합니다
# print np.array([a[0, 1], a[0, 1]])  # 출력 "[2 2]"


import numpy as np
x = np.array([[1, 2, 3], [4, 5, 6]], np.int32)
print(type(x))
print(x.shape)
print(x.dtype)