from pico2d import open_canvas, delay, close_canvas
import game_framework

import play_mode_level1 as start_mode
# import title_mode as start_mode
# import clear_mode as start_mode

open_canvas(1200, 600, sync=True)
game_framework.run(start_mode)
close_canvas()

