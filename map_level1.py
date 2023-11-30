import numpy as np
import matplotlib.pyplot as plt


# 파일을 읽어와서 Y 좌표를 저장할 리스트
y_coordinates = []

with open("levels/level1.txt", "r") as file:
    for line in file:
        y = float(line)  # 텍스트 파일에서 읽어온 문자열을 부동소수로 변환
        y_coordinates.append(y)
x_coordinates = [float(i * 100) for i in range(len(y_coordinates) * 100)]


