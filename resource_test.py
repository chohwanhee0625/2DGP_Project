from pico2d import *
import math

import world
from car import Car


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            car.handle_event(event)



def reset_world():
    global running
    global car

    running = True

    car = Car()
    world.add_object(car)


def update_world():
    world.update()


def render_world():
    clear_canvas()
    world.render()
    update_canvas()


open_canvas(1280, 600)
reset_world()
while running:
    handle_events()
    update_world()
    render_world()

    delay(0.02)

close_canvas()
