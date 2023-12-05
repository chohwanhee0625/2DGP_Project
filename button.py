from pico2d import draw_rectangle, load_image, load_wav


class Button:
    button_sound = None
    def __init__(self, image = None, x = 0, y = 0, size_x = 0, size_y = 0, flip = ''):
        self.x, self.y = x, y
        self.size_x, self.size_y = size_x // 2, size_y // 2
        self.image = load_image(image)
        self.flip = flip

        if not Button.button_sound:
            Button.button_sound = load_wav('sound/Button.wav')
            Button.button_sound.set_volume(50)

    def handle_event(self):
        pass

    def draw(self):
        self.image.composite_draw(0, self.flip, self.x, self.y, self.size_x * 2, self.size_y * 2)
        # draw_rectangle(self.x - self.size_x, self.y - self.size_y, self.x + self.size_x, self.y + self.size_y)

    def update(self):
        pass

    def get_bb(self, mx, my):   # 버튼 클릭 시 버튼 영역 확인
        if (self.x - self.size_x <= mx <= self.x + self.size_x) and (self.y - self.size_y <= my <= self.y + self.size_y):
            Button.button_sound.play()
            return True
        else:
            return False
