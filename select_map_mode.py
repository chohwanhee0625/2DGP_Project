from pico2d import *
import game_framework

import game_world
import play_mode_level1
from button import Button

buttons = []


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
                game_framework.change_mode(play_mode_level1)

def init():
    global title_image
    global buttons, game_start_button, maps

    title_image = load_image('resource/title_1.png')

    left_button = Button('resource/ArrowButton.png')
    buttons.append(left_button)

    right_button = Button('resource/ArrowButton.png')
    buttons.append(right_button)

    game_start_button = Button('resource/PlayButton.png', 600, 150, 200, 100)
    buttons.append(game_start_button)

    game_world.add_objects(buttons)

    map_1 = load_image('resource/level1.png')
    map_2 = load_image('resource/level2.png')
    map_3 = load_image('resource/level3.png')



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