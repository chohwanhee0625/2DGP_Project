from pico2d import *

open_canvas()
loading = load_image('loading.png')
player = load_image('Archery_player_1.png')
target = load_image('target_1.png')
background = load_image('background.png')



running, l_screen = True, True
frame = 0
x = 0
def handle_events():
    global running, l_screen

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            l_screen = False
            if event.key == SDLK_ESCAPE:
                running = False
        else:
            pass


while l_screen:
    clear_canvas()

    loading.composite_draw(0, '', 400, 300, 800, 600)

    update_canvas()
    handle_events()

while running:
    clear_canvas()

    background.composite_draw(0, '', 400, 300, 800, 600)
    target.composite_draw(0, '', 650, 200, 60, 67)
    player.clip_composite_draw(frame * (75 - x), 120, 100, 170, 0, '', 60, 100, 200, 340)

    update_canvas()
    handle_events()

    frame = (frame + 1) % 14
    x = (x + 1) % 15


    delay(0.07)

close_canvas()