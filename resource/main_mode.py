from pico2d import *
import game_framework

import game_world

# boy = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_MOUSEBUTTONUP and event.button == SDL_BUTTON_LEFT:
            mx, my = event.x, 600 - 1 - event.y
            if mx <= 800 and mx >= 600 and my <= 500 and my >= 300:
                pass


def init():
    running = True

    # bird = Bird()
    # game_world.add_object(bird, 1)


def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
    # delay(0.1)


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


def pause():
    pass


def resume():
    pass

