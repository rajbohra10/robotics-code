# Cylindrical Robot - Moves Linearly in X and Z, and rotates about Z

import numpy as np
import math as m
X = int(input("Enter X Coordinate: "))
Y = int(input("Enter Y Coordinate: "))
Z = int(input("Enter Z Coordinate: "))

point = np.array([[X], [Y], [Z], [1]])

tx = int(input("Enter Translation in X Axis: "))
rz = m.radians(int(input("Enter Angle of Rotation along Z Axis: ")))
print(np.sin(rz))
tz = int(input("Enter Translation in Z Axis: "))

transX = np.array([[1, 0, 0, tx], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
transZ = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, tz], [0, 0, 0, 1]])
rotZ = np.array([[np.cos(rz), -np.sin(rz), 0, 0], [np.sin(rz), np.cos(rz), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])

inter = np.matmul(transZ, rotZ)
inter = np.matmul(inter, transX)
final = np.matmul(inter, point)
print(final)