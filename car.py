from pico2d import load_image, SDL_KEYDOWN, SDL_KEYUP, SDLK_LEFT, SDLK_RIGHT

import game_framework


def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT


def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT


def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT


def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LEFT


PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Idle:

    @staticmethod
    def enter(car, e):
        car.dir = 0
        pass

    @staticmethod
    def exit(car, e):
        pass

    @staticmethod
    def do(car):
        pass

    @staticmethod
    def draw(car):
        car.image.composite_draw(0, '', car.x, car.y, 250, 125)


class Run:

    @staticmethod
    def enter(car, e):
        if right_down(e) or left_up(e):  # 오른쪽으로 RUN
            car.dir, car.face_dir = 1, 1
        elif left_down(e) or right_up(e):  # 왼쪽으로 RUN
            car.dir, car.face_dir = -1, -1

    @staticmethod
    def exit(car, e):
        pass

    @staticmethod
    def do(car):
        car.x += car.dir * RUN_SPEED_PPS * game_framework.frame_time

    @staticmethod
    def draw(car):
        car.image.composite_draw(0, '', car.x, car.y, 250, 125)


class StateMachine:
    def __init__(self, car):
        self.cur_state = Idle
        self.car = car
        self.table = {
            Idle: {right_down: Run, left_down: Run, left_up: Run, right_up: Run},
            Run: {right_down: Idle, left_down: Idle, right_up: Idle, left_up: Idle}
        }

    def start(self):
        self.cur_state.enter(self.car, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.car)

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


class Car:
    def __init__(self, x=400, y=300):
        self.x, self.y = x, y
        self.dir = 0
        self.image = load_image('resource\car_jeep_1.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()
