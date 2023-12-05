from pico2d import *
import game_framework

import game_world
import title_mode
import server
from button import Button

buttons = []


def handle_events():
    global map_count

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
        elif event.type == SDL_MOUSEBUTTONUP and event.button == SDL_BUTTON_LEFT:
            mx, my = event.x, 600 - 1 - event.y
            # print(mx, my)
            if back_button.get_bb(mx, my):
                game_framework.change_mode(title_mode)
            if engine_button.get_bb(mx, my):
                server.acceleration += 1.0
            if trans_button.get_bb(mx, my):
                server.max_speed += 10
            if wheel_button.get_bb(mx, my):
                server.roll_speed += 2




def init():
    global title_image
    global buttons, back_button, engine_button, trans_button, wheel_button

    title_image = load_image('resource/shop_bg.png')

    back_button = Button('resource/ArrowButton.png', 60, 530, 70, 70, 'h')
    buttons.append(back_button)

    engine_button = Button('resource/button_engine.png', 300, 300, 200, 200)
    buttons.append(engine_button)

    trans_button = Button('resource/button_trans.png', 600, 300, 200, 200)
    buttons.append(trans_button)

    wheel_button = Button('resource/button_wheel.png', 900, 300, 200, 200)
    buttons.append(wheel_button)

    game_world.add_objects(buttons)



def finish():
    title_mode.bgm.stop_music()
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