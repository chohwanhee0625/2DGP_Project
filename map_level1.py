from pico2d import *

class Map:
    image = None
    def __init__(self, mappath, maplist):
        if Map.image == None:
            self.image = load_image(mappath)
            self.maplist = maplist

    def draw(self):
        for x, y in self.maplist:
            self.image.draw_to_origin(x, 0, 4, y)
        pass

    def update(self):
        pass

    def handle_event(self):
        pass

