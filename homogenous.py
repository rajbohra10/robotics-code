# Homogeneous Robot - Rotates in All Directions and Translates Depending on the Frame of Reference

import numpy as np
import math as m
X = int(input("Enter X Coordinate: "))
Y = int(input("Enter Y Coordinate: "))
Z = int(input("Enter Z Coordinate: "))

point = np.array([[X], [Y], [Z], [1]])

tx = int(input("Enter Translation in X Axis: "))
ty = int(input("Enter Translation in Y Axis: "))
tz = int(input("Enter Translation in Z Axis: "))

nx = int(input("Enter X Coordinate for Reference Frame n: "))
ny = int(input("Enter Y Coordinate for Reference Frame n: "))
nz = int(input("Enter Z Coordinate for Reference Frame n: "))

ox = int(input("Enter X Coordinate for Reference Frame o: "))
oy = int(input("Enter Y Coordinate for Reference Frame o: "))
oz = int(input("Enter Z Coordinate for Reference Frame o: "))

ax = int(input("Enter X Coordinate for Reference Frame a: "))
ay = int(input("Enter Y Coordinate for Reference Frame a: "))
az = int(input("Enter Z Coordinate for Reference Frame a: "))

frame = np.array([[nx, ox, ax, 0], [ny, oy, ay, 0], [nz, oz, az, 0], [0, 0, 0, 1]])
translation = np.array([[1, 0, 0, tx], [0, 1, 0, ty], [0, 0, 1, tz], [0, 0, 0, 1]])

inter = np.matmul(translation, frame)
final = np.matmul(inter, point)
print("Homogeneous Translation\n")
print(final)

rotation = []

while True:
    axis = input("Enter Axis about which Rotation should occur: ")
    if axis == 'x' or axis == 'X':
        angle = m.radians(int(input("Enter Angle of Rotation along the Axis: ")))
        rot = np.array([[1, 0, 0, 0], [0, np.cos(angle), -np.sin(angle), 0], [0, np.sin(angle), np.cos(angle), 0], [0, 0, 0, 1]])
    elif axis == 'y' or axis == 'Y':
        angle = m.radians(int(input("Enter Angle of Rotation along the Axis: ")))
        rot = np.array([[np.cos(angle), 0, np.sin(angle), 0], [0, 1, 0, 0], [-np.sin(angle), 0, np.cos(angle), 0], [0, 0, 0, 1]])
    elif axis == 'z' or axis == 'Z':
        angle = m.radians(int(input("Enter Angle of Rotation along the Axis: ")))
        rot = np.array([[np.cos(angle), -np.sin(angle), 0, 0], [np.sin(angle), np.cos(angle), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    else:
        break
    rotation.append(rot)

inter = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])

for i in rotation:
    inter = np.matmul(inter, i)

final = np.matmul(inter, point)
print("Homogeneous Rotation\n")
print(final)