
# 파일을 읽어와서 Y 좌표를 저장할 리스트
ground_coordinates = []

with open("levels/level1.txt", "r") as file:
    for line in file:
        y = float(line)  # 텍스트 파일에서 읽어온 문자열을 부동소수로 변환
        ground_coordinates.append(y)

# print(ground_coordinates)
# print(len(ground_coordinates))
