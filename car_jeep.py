from pico2d import load_image, clamp, get_canvas_width, get_canvas_height
from sdl2 import SDL_KEYDOWN, SDLK_UP, SDL_KEYUP

import game_framework
import map_level1 as map
from background_level1 import InfiniteBackground as Background
import server

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
CAR_MAX_SPEED_KMPH = 100.0  # Km / Hour
CAR_SPEED_MPM = (CAR_MAX_SPEED_KMPH * 1000.0 / 60.0)
CAR_SPEED_MPS = (CAR_SPEED_MPM / 60.0)
CAR_SPEED_PPS = (CAR_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

GRAVITY = 9.8
ACCELERATION = 5.0


def up_button_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_UP


def up_button_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_UP


class Decelerate:
    @staticmethod
    def enter(car, e):
        # print('decel')
        pass

    @staticmethod
    def do(car):
        global FRAMES_PER_ACTION

        car.speed -= ACCELERATION
        car.speed = clamp(0, car.speed, CAR_SPEED_PPS)
        FRAMES_PER_ACTION -= 1
        FRAMES_PER_ACTION = clamp(0, FRAMES_PER_ACTION, 10)
        pass

    @staticmethod
    def exit(car, e):
        pass

    @staticmethod
    def draw(car):
        car.image.draw(car.x, car.y)


class Accelerate:
    @staticmethod
    def enter(car, e):
        # print('accel')
        pass

    @staticmethod
    def do(car):
        global FRAMES_PER_ACTION

        car.speed += ACCELERATION
        car.speed = clamp(0, car.speed, CAR_SPEED_PPS)
        FRAMES_PER_ACTION += 1
        FRAMES_PER_ACTION = clamp(0, FRAMES_PER_ACTION, 10)
        pass

    @staticmethod
    def exit(car, e):
        pass

    @staticmethod
    def draw(car):
        car.image.draw(car.x, car.y)


class StateMachine:
    def __init__(self, car):
        self.cur_state = Decelerate
        self.car = car
        self.table = {
            Decelerate: {up_button_down: Accelerate},
            Accelerate: {up_button_up: Decelerate}
        }

    def start(self):
        self.cur_state.enter(self.car, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.car)
        self.car.frame = (self.car.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        self.car.x += self.car.speed * game_framework.frame_time
        self.car.y -= 0.5 * GRAVITY * game_framework.tick_count * game_framework.tick_count
        self.car.y = clamp(100, self.car.y, server.background.h - 100)

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
        self.speed = 0
        self.frame = 0
        self.image = load_image('resource/car_sheet.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()
        game_framework.tick_count = 0

    def draw(self):
        sx = self.x - server.background.window_left
        sy = self.y - server.background.window_bottom
        self.image.clip_draw(int(self.frame) * 182, 0, 182, 137, sx, sy)

    def update(self):
        self.state_machine.update()
        self.x = clamp(50, self.x, server.background.w - 50)
        self.y = clamp(50, self.y, server.background.h - 50)

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def get_bb(self):
        pass
