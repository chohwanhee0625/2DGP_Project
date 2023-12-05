from pico2d import *

import game_framework
import game_world
import select_map_mode

from button import Button

buttons = []

class BGM:
    bgm = None
    def __init__(self):
        if not BGM.bgm:
            BGM.bgm = load_music('sound/Background.mp3')
            BGM.bgm.set_volume(40)

    def handle_event(self):
        pass
    def draw(self):
        pass
    def update(self):
        pass
    def stop_music(self):
        BGM.bgm.stop()
    def start_music(self):
        BGM.bgm.repeat_play()



def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_MOUSEBUTTONUP and event.button == SDL_BUTTON_LEFT:
            mx, my = event.x, 600 - 1 - event.y
            # print(mx, my)
            if game_start_button.get_bb(mx, my):
                game_framework.change_mode(select_map_mode)


def init():
    global title_image
    global buttons, game_start_button, bgm

    title_image = load_image('resource/title_1.png')

    game_start_button = Button('resource/PlayButton.png', 200, 300, 291, 163)
    buttons.append(game_start_button)

    car_select_button = Button('resource/CarSelectButton.png', 100, 130, 160, 160)
    buttons.append(car_select_button)

    select_button = Button('resource/button_base_s.png', 300, 130, 160, 160)
    buttons.append(select_button)

    game_world.add_objects(buttons)

    bgm = BGM()
    game_world.add_object(bgm)
    bgm.start_music()


def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
    # delay(0.1)


def draw():
    clear_canvas()
    title_image.composite_draw(0, '', 600, 300, 1200, 600)
    game_world.render()
    update_canvas()


def pause():
    pass


def resume():
    pass



