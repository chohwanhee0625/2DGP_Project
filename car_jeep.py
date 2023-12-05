import math

from pico2d import load_image, clamp, get_canvas_width, get_canvas_height, load_wav
from sdl2 import SDL_KEYDOWN, SDLK_UP, SDL_KEYUP, SDLK_RIGHT, SDLK_LEFT

import game_framework
import map as map
from background import InfiniteBackground as Background
import server

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
CAR_MAX_SPEED_KMPH = 100.0  # Km / Hour
CAR_SPEED_MPM = (CAR_MAX_SPEED_KMPH * 1000.0 / 60.0)
CAR_SPEED_MPS = (CAR_SPEED_MPM / 60.0)
CAR_SPEED_PPS = (CAR_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

GRAVITY = 5.0
ACCELERATION = 5.0


def up_button_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_UP
def up_button_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_UP
def right_button_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT
def right_button_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT
def left_button_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LEFT
def left_button_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT



class Decelerate:
    @staticmethod
    def enter(car, e):
        print('decel')
        car.car_sound = load_wav('sound/EngineIdling.wav')
        car.car_sound.repeat_play()
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
        car.car_sound = load_wav('sound/AcceleEnter.wav')
        car.car_sound.repeat_play()
        print('accel')
        pass

    @staticmethod
    def do(car):
        global FRAMES_PER_ACTION

        car.speed += ACCELERATION
        car.speed = clamp(0, car.speed, CAR_SPEED_PPS)
        FRAMES_PER_ACTION += 1
        FRAMES_PER_ACTION = clamp(0, FRAMES_PER_ACTION, 10)

        # car.car_sound = load_wav('sound/MaxSpeed.wav')
        # car.car_sound.play()
        pass

    @staticmethod
    def exit(car, e):
        pass

    @staticmethod
    def draw(car):
        car.image.draw(car.x, car.y)


class RollFront:
    @staticmethod
    def enter(car, e):
        print('rollfront')
        car.car_sound = load_wav('sound/EngineIdling.wav')
        car.car_sound.repeat_play()
        pass

    @staticmethod
    def do(car):
        car.dir -= math.radians(2)
        pass

    @staticmethod
    def exit(car, e):
        pass

    @staticmethod
    def draw(car):
        car.image.draw(car.x, car.y)


class RollBack:
    @staticmethod
    def enter(car, e):
        print('rollback')
        car.car_sound = load_wav('sound/EngineIdling.wav')
        car.car_sound.repeat_play()
        pass

    @staticmethod
    def do(car):
        car.dir += math.radians(2)
        pass

    @staticmethod
    def exit(car, e):
        pass

    @staticmethod
    def draw(car):
        car.image.draw(car.x, car.y)

class RollFrontAcc:
    @staticmethod
    def enter(car, e):
        car.car_sound = load_wav('sound/AcceleEnter.wav')
        car.car_sound.repeat_play()
        print('rollfrontacc')
        pass

    @staticmethod
    def do(car):
        global FRAMES_PER_ACTION

        car.speed += ACCELERATION
        car.speed = clamp(0, car.speed, CAR_SPEED_PPS)
        FRAMES_PER_ACTION += 1
        FRAMES_PER_ACTION = clamp(0, FRAMES_PER_ACTION, 10)

        car.dir -= math.radians(2)
        pass

    @staticmethod
    def exit(car, e):
        pass

    @staticmethod
    def draw(car):
        car.image.draw(car.x, car.y)

class RollBackAcc:
    @staticmethod
    def enter(car, e):
        car.car_sound = load_wav('sound/AcceleEnter.wav')
        car.car_sound.repeat_play()
        print('rollbackacc')
        pass

    @staticmethod
    def do(car):
        global FRAMES_PER_ACTION

        car.speed += ACCELERATION
        car.speed = clamp(0, car.speed, CAR_SPEED_PPS)
        FRAMES_PER_ACTION += 1
        FRAMES_PER_ACTION = clamp(0, FRAMES_PER_ACTION, 10)

        car.dir += math.radians(2)
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
            Decelerate: {up_button_down: Accelerate,
                         left_button_down: RollBack, right_button_down: RollFront},
            Accelerate: {up_button_up: Decelerate,
                         left_button_down: RollBackAcc, right_button_down: RollFrontAcc},
            RollBack: {up_button_down: RollBackAcc, left_button_up: Decelerate, right_button_down: RollFront},
            RollFront: {up_button_down: RollFrontAcc, right_button_up: Decelerate, left_button_down: RollBack},
            RollBackAcc: {up_button_up: RollBack, left_button_up: Accelerate, right_button_down: RollFrontAcc},
            RollFrontAcc: {up_button_up: RollFront, right_button_up: Accelerate, left_button_down: RollBackAcc}
        }

    def start(self):
        self.cur_state.enter(self.car, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.car)
        self.car.frame = (self.car.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        self.car.x += self.car.speed * game_framework.frame_time

        if self.car.y >= server.map.maplist[self.car.find_closest_key(self.car.x)] + 50:
            self.car.y -= (0.5 * GRAVITY * game_framework.tick_count * game_framework.tick_count
                           * game_framework.frame_time * 100)
            # self.car.y = clamp(150, self.car.y, server.background.h)
        else:
            game_framework.tick_count = 0
            self.car.y = server.map.maplist[self.car.find_closest_key(self.car.x)] + 50
            dx = 160
            dy = server.map.maplist[self.car.find_closest_key(self.car.x + 80)] - server.map.maplist[
                self.car.find_closest_key(self.car.x - 80)]
            self.car.dir = math.atan2(dy, dx)



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
    car_sound = None
    def __init__(self):
        self.x, self.y = 250, 300
        self.speed = 0
        self.frame = 0
        self.image = load_image('resource/car_sheet.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()
        self.dir = 0.0
        game_framework.tick_count = 0

        if not Jeep.car_sound:
            Jeep.car_sound = load_wav('sound/EngineStart.wav')
            Jeep.car_sound.set_volume(30)
            Jeep.car_sound.play()

    def draw(self):
        if self.x <= get_canvas_width() // 2:
            sx = self.x
        else:
            sx = get_canvas_width() // 2

        self.image.clip_composite_draw(int(self.frame) * 180, 0, 182, 137, self.dir, '', sx, self.y, 182, 137)


    def update(self):
        self.state_machine.update()
        # self.dir = ???    # map 에서 두 바퀴에 해당하는 좌표값 2개 읽어와서 뺄셈 <x, y> , self.dir = atan2(y/x)

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def get_bb(self):
        pass

    def find_closest_key(self, target):
        closest_key = min(server.map.maplist, key=lambda x: abs(x - target))
        return closest_key


