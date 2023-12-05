from pico2d import *
import game_framework

import game_world
import play_mode_level1
import play_mode_level2
import play_mode_level3
import title_mode
from button import Button

buttons = []


def handle_events():
    global map_count

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_MOUSEBUTTONUP and event.button == SDL_BUTTON_LEFT:
            mx, my = event.x, 600 - 1 - event.y
            # print(mx, my)
            if left_button.get_bb(mx, my):
                map_count -= 1
            if right_button.get_bb(mx, my):
                map_count += 1

            if game_start_button.get_bb(mx, my) and map_count % 3 == 0:
                game_framework.change_mode(play_mode_level1)
            elif game_start_button.get_bb(mx, my) and map_count % 3 == 1:
                game_framework.change_mode(play_mode_level2)
            elif game_start_button.get_bb(mx, my) and map_count % 3 == 2:
                game_framework.change_mode(play_mode_level3)



def init():
    global title_image, map_1, map_2, map_3
    global buttons, game_start_button, maps, left_button, right_button
    global map_count

    map_count = 0

    title_image = load_image('resource/title_1.png')

    left_button = Button('resource/Arrow.png', 200, 300, 50, 50)
    buttons.append(left_button)

    right_button = Button('resource/Arrow.png', 1000, 300, 50, 50, 'h')
    buttons.append(right_button)

    game_start_button = Button('resource/PlayButton.png', 600, 100, 200, 100)
    buttons.append(game_start_button)

    game_world.add_objects(buttons)

    map_1 = load_image('resource/level1.png')
    map_2 = load_image('resource/level2.png')
    map_3 = load_image('resource/level3.png')




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
    if map_count % 3 == 0:
        map_1.composite_draw(0, '', 600, 300, 600, 300)
    elif map_count % 3 == 1:
        map_2.composite_draw(0, '', 600, 300, 600, 300)
    elif map_count % 3 == 2:
        map_3.composite_draw(0, '', 600, 300, 600, 300)

    game_world.render()
    update_canvas()


def pause():
    pass


def resume():
    pass