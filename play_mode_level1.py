from pico2d import *
import game_framework

import game_world
import title_mode
from car_jeep import Jeep


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
        else:
            car.handel_event(event)


def init():
    global bg_image
    global car

    bg_image = load_image('resource/level1bg.png')

    car = Jeep()
    game_world.add_object(car, 1)



def finish():
    game_world.clear()


def update():
    game_world.update()


def draw():
    clear_canvas()
    bg_image.composite_draw(0, '', 600, 300, 1200, 600)
    game_world.render()
    update_canvas()


def pause():
    pass


def resume():
    pass
