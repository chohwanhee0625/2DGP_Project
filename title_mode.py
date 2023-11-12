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
    global buttons, game_start_button

    title_image = load_image('resource/title.png')

    game_start_button = Button('resource/PlayButton.png', 200, 300, 291, 163)
    buttons.append(game_start_button)

    car_select_button = Button('resource/CarSelectButton.png', 100, 130, 160, 160)
    buttons.append(car_select_button)



def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
    # delay(0.1)


def draw():
    clear_canvas()
    title_image.composite_draw(0, '', 600, 300, 1200, 600)
    for b in buttons:
        b.draw()
    update_canvas()


def pause():
    pass


def resume():
    pass



