from pico2d import *

import server


class Map:
    image = None
    finishline = None
    def __init__(self, mappath, maplist):
        if Map.image == None:
            self.image = load_image(mappath)
            self.maplist = maplist
        if Map.finishline == None:
            self.finishline = load_image('resource/finishline.png')

    def draw(self):
        for x, y in self.maplist.items():
            sx, sy = x - (server.car.x - 600), y
            if server.car.x - 600 <= x <= server.car.x + 600:
                self.image.draw_to_origin(sx, 0, 4, sy)

        fx = max(self.maplist.keys()) - server.car.x + 600
        self.finishline.draw_to_origin(fx, 0, 100, 100)

        pass

    def update(self):
        pass

    def handle_event(self):
        pass

