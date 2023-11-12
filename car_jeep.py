
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
CAR_SPEED_KMPH = 20.0  # Km / Hour
CAR_SPEED_MPM = (CAR_SPEED_KMPH * 1000.0 / 60.0)
CAR_SPEED_MPS = (CAR_SPEED_MPM / 60.0)
CAR_SPEED_PPS = (CAR_SPEED_MPS * PIXEL_PER_METER)


class Jeep:
    def __init__(self):
        pass

    def draw(self):
        pass

    def update(self):
        pass

    def get_bb(self):
        pass
