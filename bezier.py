import numpy as np


def cubic_bezier(t, p0, p1, p2, p3):
    return (1 - t) ** 3 * p0 + 3 * (1 - t) ** 2 * t * p1 + 3 * (1 - t) * t ** 2 * p2 + t ** 3 * p3

def Bezier(filepath):
    # 파일을 읽어와서 Y 좌표를 저장할 리스트
    y_coords = []

    with open(filepath, "r") as file:
        for line in file:
            y = float(line)  # 텍스트 파일에서 읽어온 문자열을 부동소수로 변환
            y_coords.append(y)

    x_coords = [float(i * 100) for i in range(len(y_coords))]

    # print(len(y_coords))
    # print(len(x_coords))

    curve_points = []
    for i in range(0, len(x_coords) - 3, 3):
        p0 = np.array([x_coords[i], y_coords[i]])
        p1 = np.array([x_coords[i + 1], y_coords[i + 1]])
        p2 = np.array([x_coords[i + 2], y_coords[i + 2]])
        p3 = np.array([x_coords[i + 3], y_coords[i + 3]])
        # t 값을 0에서 1까지 등간격으로 생성
        t_values = np.linspace(0, 1, 100)
        # 베지어 곡선 상의 점들 계산
        curve_points.extend([cubic_bezier(t, p0, p1, p2, p3) for t in t_values])

    # 베지어 곡선 상의 x, y 좌표
    curve_x = np.array(curve_points)[:, 0]
    curve_y = np.array(curve_points)[:, 1]



    # 베지어 곡선 상의 x, y 좌표를 출력 (테스트용)
    # for i in range(len(curve_x)):
    #     print(f"({curve_x[i]}, {curve_y[i]})")
    # print(len(curve_x))

    # 정수로 변환된 (x, y) 좌표를 튜플 리스트로 반환
    return list(zip(map(int, curve_x), map(int, curve_y)))
    # return dict(zip(curve_x, curve_y))    # 고민중

# data = Bezier("levels/level1.txt")
# print(data)


