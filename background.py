from pico2d import *

import server


class FixedBackground:
    def __init__(self):
        self.image = load_image('resource/level1bg.png')
        self.w = self.image.w
        self.h = self.image.h  # 배경 이미지의 너비, 높이

        self.cw = get_canvas_width()  # 캔버스의 너비
        self.ch = get_canvas_height()  # 캔버스의 높이
        # fill here
        pass

    def draw(self):
        # fill here
        self.image.clip_draw_to_origin(self.window_left, self.window_bottom,
                                       self.cw, self.ch, 0, 0)
        pass

    def update(self):
        # fill here
        self.window_left = int(server.car.x) - self.cw // 2
        self.window_bottom = int(server.car.y) - self.ch // 2

        self.window_left = clamp(0, self.window_left, self.w - self.cw - 1)
        self.window_bottom = clamp(0, self.window_bottom, self.h - self.ch - 1)
        pass

    def handle_event(self, event):
        pass


class TileBackground:

    def __init__(self):
        self.cw = get_canvas_width()
        self.ch = get_canvas_height()
        self.w = 800 * 3
        self.h = 600 * 3

        # fill here

    def update(self):
        pass

    def draw(self):
        self.window_left = clamp(0, int(server.boy.x) - self.cw // 2, self.w - self.cw - 1)
        self.window_bottom = clamp(0, int(server.boy.y) - self.ch // 2, self.h - self.ch - 1)

        # fill here
        pass


cx = 900 % 800
cy = 700 // 600


class InfiniteBackground:

    def __init__(self, imagePath = None):
        self.image = load_image(imagePath)
        self.cw = get_canvas_width()
        self.ch = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h

    def draw(self):
        self.image.clip_draw_to_origin(self.q3l, self.q3b, self.q3w, self.q3h, 0, 0)  # quadrant 3
        self.image.clip_draw_to_origin(self.q2l, self.q2b, self.q2w, self.q2h, self.q3w, 0)  # quadrant 2

    def update(self):
        # quadrant 3
        self.q3l = (int(server.car.x) - self.cw // 2) % self.w
        self.q3b = 0
        self.q3w = clamp(0, self.w - self.q3l, self.w)
        self.q3h = self.ch

        # quadrant 2
        self.q2l = 0
        self.q2b = 0
        self.q2w = self.cw - self.q3w
        self.q2h = self.ch

    def handle_event(self, event):
        pass
