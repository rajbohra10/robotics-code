# Cartesian Robot - Moves Linearly in X, Y and Z

import numpy as np
X = int(input("Enter X Coordinate: "))
Y = int(input("Enter Y Coordinate: "))
Z = int(input("Enter Z Coordinate: "))

point = np.array([[X], [Y], [Z], [1]])

tx = int(input("Enter Translation in X Axis: "))
ty = int(input("Enter Translation in Y Axis: "))
tz = int(input("Enter Translation in Z Axis: "))

translation = np.array([[1, 0, 0, tx], [0, 1, 0, ty], [0, 0, 1, tz], [0, 0, 0, 1]])

final = np.matmul(translation, point)
print(final)

