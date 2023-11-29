from pico2d import load_image, clamp, get_canvas_width, get_canvas_height
from sdl2 import SDL_KEYDOWN, SDLK_UP, SDL_KEYUP

import game_framework
import map_level1 as map
import background_level1 as background

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
CAR_SPEED_KMPH = 50.0  # Km / Hour
CAR_SPEED_MPM = (CAR_SPEED_KMPH * 1000.0 / 60.0)
CAR_SPEED_MPS = (CAR_SPEED_MPM / 60.0)
CAR_SPEED_PPS = (CAR_SPEED_MPS * PIXEL_PER_METER)

GRAVITY = 9.8
FRAME_COUNT = 0


def up_button_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_UP


def up_button_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_UP


class Deceleration:
    @staticmethod
    def enter(car, e):
        # print('decel')
        car.speed = 0
        pass

    @staticmethod
    def do(car):
        pass

    @staticmethod
    def exit(car, e):
        pass

    @staticmethod
    def draw(car):
        car.image.draw(car.x, car.y)


class Acceleration:
    @staticmethod
    def enter(car, e):
        # print('accel')
        car.speed = CAR_SPEED_PPS
        pass

    @staticmethod
    def do(car):
        pass

    @staticmethod
    def exit(car, e):
        pass

    @staticmethod
    def draw(car):
        car.image.draw(car.x, car.y)


class StateMachine:
    def __init__(self, car):
        self.cur_state = Deceleration
        self.car = car
        self.table = {
            Deceleration: {up_button_down: Acceleration},
            Acceleration: {up_button_up: Deceleration}
        }

    def start(self):
        self.cur_state.enter(self.car, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.car)
        self.car.x = self.car.speed * game_framework.frame_time()

    def handle_event(self, e):
        for check_event, next_state in self.table[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.car, e)
                self.cur_state = next_state
                self.cur_state.enter(self.car, e)
                return True

        return False

    def draw(self):
        self.cur_state.draw(self.car)


class Jeep:
    def __init__(self):
        self.x, self.y = 250, 300
        self.image = load_image('resource/car_jeep.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()
        game_framework.tick_count = 0

    def draw(self):
        sx, sy = get_canvas_width() // 2, get_canvas_height() // 2
        self.image.draw(sx, sy)

    def update(self):
        # print(f'{self.x}, {self.y}')
        # if self.y >= 100:
        #     self.y -= 0.5 * GRAVITY * game_framework.tick_count * game_framework.tick_count
        # else:
        #     game_framework.tick_count = 0
        # self.y = clamp(100, self.y, background.bh - 100)
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def get_bb(self):
        pass
