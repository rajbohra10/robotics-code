# Composite Robot - Allows Everything

import numpy as np
import math as m
X = int(input("Enter X Coordinate: "))
Y = int(input("Enter Y Coordinate: "))
Z = int(input("Enter Z Coordinate: "))

point = np.array([[X], [Y], [Z], [1]])
fixed = []
movable = []
print("Enter operations for Fixed Axis: ")
while True:
    print("1. Translation")
    print("2. Rotation")
    print("3. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        axis = input("Enter Translation Axis: ")
        value = int(input("Enter Translation Value"))
        if axis == 'x' or axis == 'X':
            trans = np.array([[1, 0, 0, value], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
            fixed.append(trans)
        elif axis == 'y' or axis == 'Y':
            trans = np.array([[1, 0, 0, 0], [0, 1, 0, value], [0, 0, 1, 0], [0, 0, 0, 1]])
            fixed.append(trans)
        elif axis == 'z' or axis == 'Z':
            trans = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, value], [0, 0, 0, 1]])
            fixed.append(trans)
    elif ch == 2:
        axis = input("Enter Axis about which Rotation should occur: ")
        if axis == 'x' or axis == 'X':
            angle = m.radians(int(input("Enter Angle of Rotation along the Axis: ")))
            rot = np.array([[1, 0, 0, 0], [0, np.cos(angle), -np.sin(angle), 0], [0, np.sin(angle), np.cos(angle), 0], [0, 0, 0, 1]])
            fixed.append(rot)
        elif axis == 'y' or axis == 'Y':
            angle = m.radians(int(input("Enter Angle of Rotation along the Axis: ")))
            rot = np.array([[np.cos(angle), 0, np.sin(angle), 0], [0, 1, 0, 0], [-np.sin(angle), 0, np.cos(angle), 0], [0, 0, 0, 1]])
            fixed.append(rot)
        elif axis == 'z' or axis == 'Z':
            angle = m.radians(int(input("Enter Angle of Rotation along the Axis: ")))
            rot = np.array([[np.cos(angle), -np.sin(angle), 0, 0], [np.sin(angle), np.cos(angle), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
            fixed.append(rot)
    elif ch == 3:
        break

print("Enter operations for Movable Axis: ")
while True:
    print("1. Translation")
    print("2. Rotation")
    print("3. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        axis = input("Enter Translation Axis: ")
        value = int(input("Enter Translation Value"))
        if axis == 'n' or axis == 'N':
            trans = np.array([[1, 0, 0, value], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
            movable.append(trans)
        elif axis == 'o' or axis == 'O':
            trans = np.array([[1, 0, 0, 0], [0, 1, 0, value], [0, 0, 1, 0], [0, 0, 0, 1]])
            movable.append(trans)
        elif axis == 'a' or axis == 'A':
            trans = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, value], [0, 0, 0, 1]])
            movable.append(trans)
    elif ch == 2:
        axis = input("Enter Axis about which Rotation should occur: ")
        if axis == 'n' or axis == 'N':
            angle = m.radians(int(input("Enter Angle of Rotation along the Axis: ")))
            rot = np.array([[1, 0, 0, 0], [0, np.cos(angle), -np.sin(angle), 0], [0, np.sin(angle), np.cos(angle), 0], [0, 0, 0, 1]])
            movable.append(rot)
        elif axis == 'o' or axis == 'O':
            angle = m.radians(int(input("Enter Angle of Rotation along the Axis: ")))
            rot = np.array([[np.cos(angle), 0, np.sin(angle), 0], [0, 1, 0, 0], [-np.sin(angle), 0, np.cos(angle), 0], [0, 0, 0, 1]])
            movable.append(rot)
        elif axis == 'a' or axis == 'A':
            angle = m.radians(int(input("Enter Angle of Rotation along the Axis: ")))
            rot = np.array([[np.cos(angle), -np.sin(angle), 0, 0], [np.sin(angle), np.cos(angle), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
            movable.append(rot)
    elif ch == 3:
        break

fixed.reverse()

inter = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
for i in fixed:
    inter = np.matmul(inter, i)

for i in movable:
    inter = np.matmul(inter, i)

final = np.matmul(inter, point)
print(final)