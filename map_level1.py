from pico2d import *

from bezier import Bezier

map_level1 = Bezier("levels/level1.txt")
# print(map_level1)

class Map:
    image = None
    def __init__(self, mappath):
        if Map.image == None:
            self.image = load_image(mappath)
            self.x = 0
            self.y = 0

    def draw(self):
        self.image.draw_to_origin(self.x, 0, 3, self.y)
        pass

    def update(self):
        pass

    def handle_event(self):
        pass

