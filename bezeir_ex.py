import numpy as np
import matplotlib.pyplot as plt

# 주어진 y좌표 배열을 사용하여 베지에 곡선을 생성하는 함수
def bezier_curve(y_coords):
    n = len(y_coords) - 1
    x = np.linspace(0, 100, len(y_coords))  # 100 간격으로 x좌표 생성
    result = np.zeros((len(x), 2))

    for i, t in enumerate(np.linspace(0, 1, len(x))):
        temp = np.zeros((n + 1, 2))
        temp[:, 1] = y_coords  # 주어진 y좌표 배열을 temp 배열의 y좌표로 설정

        for r in range(1, n + 1):
            for i in range(n - r + 1):
                temp[i] = (1 - t) * temp[i] + t * temp[i + 1]

        result[i] = temp[0]  # 결과에 베지에 곡선의 좌표 저장

    return result

# 예시로 주어진 y좌표 배열
y_coords = np.array([0, 3, 1, 4, 2])

# 베지에 곡선 생성
curve_points = bezier_curve(y_coords)

# 결과 출력
plt.plot(curve_points[:, 0], curve_points[:, 1], label='Bezier Curve', marker='o')
plt.scatter(range(len(y_coords)), y_coords, color='red', label='Control Points')
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Bezier Curve with Control Points')
plt.grid(True)
plt.show()
