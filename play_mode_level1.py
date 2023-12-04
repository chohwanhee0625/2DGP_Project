from pico2d import *

import game_framework
import game_world
import title_mode
import server
from bezier import Bezier

from car_jeep import Jeep
from background import InfiniteBackground as Background
from map_level1 import Map



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
    server.background = Background('resource/level1bg.png')
    game_world.add_object(server.background, 0)

    server.car = Jeep()
    game_world.add_object(server.car, 2)

    map_level1 = Bezier("levels/level1.txt")
    server.map = Map('resource/level1ground.png', map_level1)
    game_world.add_object(server.map, 1)


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
