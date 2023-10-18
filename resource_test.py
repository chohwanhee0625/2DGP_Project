from pico2d import *
import math


def handle_events():
    global running
    global dir

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.key == SDLK_RIGHT:
            if event.type == SDL_KEYDOWN: dir = 1
            else: dir = 0
        elif event.key == SDLK_LEFT:
            if event.type == SDL_KEYDOWN: dir = -1
            else: dir = 0



def reset_world():
    global running
    global c_x, c_y, car, dir

    running = True
    dir = 0
    car = load_image('resource\car_jeep_1.png')
    c_x, c_y = 0, 30


def update_world():
    global dir, c_x

    c_x += dir*10


def render_world():
    global c_x, c_y, car

    clear_canvas()
    car.composite_draw(0, '', c_x, c_y, 250, 125)
    update_canvas()


open_canvas(1280, 600)
reset_world()
while running:
    handle_events()
    update_world()
    render_world()

    delay(0.03)

close_canvas()
