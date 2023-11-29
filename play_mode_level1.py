from pico2d import *
import game_framework

import game_world
import title_mode
from car_jeep import Jeep
from background_level1 import InfiniteBackground as Background
import server


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
        else:
            server.car.handle_event(event)


def init():
    server.background = Background()
    game_world.add_object(server.background, 0)

    server.car = Jeep()
    game_world.add_object(server.car, 1)



def finish():
    game_world.clear()


def update():
    game_world.update()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


def pause():
    pass


def resume():
    pass
