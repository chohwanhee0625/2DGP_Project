# # 텍스트 파일 열기
# with open("levels/level3.txt", "r") as file:
#     lines = file.readlines()
#
# # 각 줄의 부동소수점 숫자를 읽어와서 변환하여 새로운 값을 계산하고 리스트에 저장
# new_numbers = []
# for line in lines:
#     try:
#         number = float(line.strip())
#         new_number = (number * 30) + 100
#         new_numbers.append(new_number)
#     except ValueError:
#         print(f"Wrong type: {line.strip()}")
#
# with open("levels/level3.txt", "w") as file:
#     for new_number in new_numbers:
#         file.write(str(new_number) + "\n")
#
# print("변환 저장 성공!.")
