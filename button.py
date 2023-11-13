from pico2d import draw_rectangle, load_image


class Button:
    def __init__(self, image = None, x = None, y = None, size_x = None, size_y = None):
        self.x, self.y = x, y
        self.size_x, self.size_y = size_x // 2, size_y // 2
        self.image = load_image(image)

    def handle_event(self):
        pass

    def draw(self):
        self.image.composite_draw(0, '', self.x, self.y, self.size_x * 2, self.size_y * 2)
        draw_rectangle(self.x - self.size_x, self.y - self.size_y, self.x + self.size_x, self.y + self.size_y)

    def update(self):
        pass

    def get_bb(self, mx, my):   # 버튼 클릭 시 버튼 영역 확인

        if (self.x - self.size_x <= mx <= self.x + self.size_x) and (self.y - self.size_y <= my <= self.y + self.size_y):
            return True
        else:
            return False
