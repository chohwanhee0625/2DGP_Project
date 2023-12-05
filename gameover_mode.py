from pico2d import *
import game_framework

import game_world
import server
import title_mode


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.pop_mode()
            game_framework.change_mode(title_mode)


def init():
    global gameover_time, font, image

    font = load_font('resource/dpcomic.ttf', 50)

    image = load_image('resource/gameoverbg.png')

    sound = load_wav('sound/Gameover.wav')
    sound.set_volume(30)
    sound.play()

    print(f'{gameover_time}s')

    pass

def finish():
    game_world.clear()
    pass


def update():
    game_world.update()


def draw():
    clear_canvas()
    game_world.render()
    image.composite_draw(0, '', 600, 300, 600, 300)
    font.draw(400, 50, 'Exit to press \'ESC\'')
    font.draw(550, 100, f'{gameover_time:.2f}s')
    update_canvas()


def pause():
    pass


def resume():
    pass
