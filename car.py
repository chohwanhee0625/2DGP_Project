from pico2d import load_image

class StateMachine:
    def __init__(self, car):
        self.cur_state = Idle
        self.car = car
        self.table = {
        }


class Car:
    def __init__(self):
        self.x, self.y = 400, 300
        self.dir = 0
        self.image = load_image('car_jeep.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()
