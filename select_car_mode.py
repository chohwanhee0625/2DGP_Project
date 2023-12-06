from pico2d import *
import game_framework

import game_world
import server
import title_mode
from button import Button

buttons = []


def handle_events():
    global car_count

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
            if left_button.get_bb(mx, my):
                car_count -= 1
            if right_button.get_bb(mx, my):
                car_count += 1
            if start_button.get_bb(mx, my):
                game_framework.change_mode(title_mode)


def init():
    global title_image
    global buttons, left_button, right_button, back_button, car_count, start_button
    global car_1, car_2, car_3

    car_count = 0

    title_image = load_image('resource/title_1.png')

    left_button = Button('resource/Arrow.png', 200, 300, 50, 50)
    buttons.append(left_button)

    right_button = Button('resource/Arrow.png', 1000, 300, 50, 50, 'h')
    buttons.append(right_button)

    back_button = Button('resource/ArrowButton.png', 60, 530, 70, 70, 'h')
    buttons.append(back_button)

    start_button = Button('resource/PlayButton.png', 600, 100, 200, 100)
    buttons.append(start_button)

    game_world.add_objects(buttons)

    car_1 = load_image('resource/jeep_select.png')
    car_2 = load_image('resource/truck_select.png')
    car_3 = load_image('resource/racingcar_select.png')




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
    if car_count % 3 == 0:
        server.car_image = 'resource/jeep_sheet.png'
        car_1.composite_draw(0, '', 600, 300, 600, 300)
    elif car_count % 3 == 1:
        server.car_image = 'resource/truck_sheet.png'
        car_2.composite_draw(0, '', 600, 300, 600, 300)
    elif car_count % 3 == 2:
        server.car_image = 'resource/racingcar_sheet.png'
        car_3.composite_draw(0, '', 600, 300, 600, 300)
    game_world.render()
    update_canvas()


def pause():
    pass


def resume():
    pass