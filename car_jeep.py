from pico2d import load_image

import game_framework

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
CAR_SPEED_KMPH = 0.7  # Km / Hour
CAR_SPEED_MPM = (CAR_SPEED_KMPH * 1000.0 / 60.0)
CAR_SPEED_MPS = (CAR_SPEED_MPM / 60.0)
CAR_SPEED_PPS = (CAR_SPEED_MPS * PIXEL_PER_METER)
GRAVITY = -0.01


class Jeep:
    def __init__(self):
        self.x, self.y = 300, 300
        self.image = load_image('resource/car_jeep.png')
        self.tick = 0
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        print(f'{self.x}, {self.y}')
        if self.y >= 100:
            self.y -= (CAR_SPEED_PPS * game_framework.tick_count
                       + 0.5 * GRAVITY * game_framework.tick_count * game_framework.tick_count)

    def get_bb(self):
        pass
