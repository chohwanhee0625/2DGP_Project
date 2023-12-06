import random

from pico2d import *
import game_world
import server


class Coin:
    image = None
    sound = None
    def __init__(self, x, y):
        if Coin.image == None:
            self.image = load_image('resource/Coin.png')
        self.x = x if x else random.randint(300, max(server.maplist.keys()) - 600)
        self.y = y + 50
        if Coin.sound == None:
            Coin.sound = load_wav('sound/pickup.wav')
            Coin.sound.set_volume(30)

    def draw(self):
        sx = self.x - server.car.x + 600
        sy = self.y
        self.image.composite_draw(0, '', sx, sy, 40, 40)
        pass

    def update(self):
        pass

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def handle_collision(self, group, other):
        match group:
            case 'car:coin':
                print('coin')
                server.coin_count += 1
                Coin.sound.play()
                game_world.remove_object(self)

