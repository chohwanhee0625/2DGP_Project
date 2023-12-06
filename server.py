
car = None
background = None
map = None
coin_count = 0

selection = 0
model_x = 0

jeep_image = 'resource/jeep_sheet.png'
truck_image = 'resource/truck_sheet.png'
racingcar_image = 'resource/racingcar_sheet.png'

jeep_x = 180
truck_x = 178
racingcar_x = 183


if selection % 3 == 0:
    model_x = jeep_x
    car_image = jeep_image
elif selection % 3 == 1:
    model_x = truck_x
    car_image = truck_image
elif selection % 3 == 2:
    model_x = racingcar_x
    car_image = racingcar_image

acceleration = 5.0
max_speed = 70.0
roll_speed = 30

