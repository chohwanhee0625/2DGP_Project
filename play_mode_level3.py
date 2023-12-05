from pico2d import *

import clear_mode
import game_framework
import game_world
import gameover_mode
import title_mode
import server
from bezier import Bezier

from car import CAR
from background import InfiniteBackground as Background
from map import Map



def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            server.car.car_sound = None
            title_mode.bgm.start_music()
            game_framework.change_mode(title_mode)
        else:
            server.car.handle_event(event)


def init():
    global start_time, font

    server.background = Background('resource/level3bg.png')
    game_world.add_object(server.background, 0)

    server.car = CAR()
    game_world.add_object(server.car, 2)

    map_level3 = Bezier("levels/level3.txt")
    server.map = Map('resource/level3ground.png', map_level3)
    game_world.add_object(server.map, 1)

    start_time = get_time()
    font = load_font('resource/dpcomic.ttf', 35)


def finish():
    game_world.clear()


def update():
    global time_now
    time_now = get_time() - start_time

    if server.car.x >= max(server.map.maplist.keys()):
        print('clear')
        finish_time = get_time() - start_time
        print(f'{finish_time:.2f}s')
        server.car.car_sound = None
        game_framework.change_mode(clear_mode)

    if server.car.y <= server.map.maplist[server.car.find_closest_key(server.car.x)] + 80:
        if math.pi / 2.0 <= server.car.dir % math.pi * 2 <= math.pi * 3.0 / 2.0:
            gameover_mode.gameover_time = time_now
            game_framework.push_mode(gameover_mode)

    game_world.update()


def draw():
    clear_canvas()
    game_world.render()

    font.draw(20, 570, f'{time_now:.2f}s', (0, 0, 0))

    update_canvas()


def pause():
    pass


def resume():
    pass
