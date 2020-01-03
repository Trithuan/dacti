from keyboard import *
from threading import Timer
class FallingKey:

    def __init__(self, key, col, w, h, speed):
        self.key = key
        self.finger = self.finger()
        self.width = w/8
        self.height = h/8
        self.x = self.get_x()
        self.y = 0
        self.first = True
        self.speed = speed
        self.color = col
        self.primeColor = col
        self.mustclick = False
        self.clicked = False
        self.clickable = False
        self.nosibling = True
        self.unused = True
        self.perfect = False
        self.lost = False

    def fall(self):
        self.y += self.speed

    def get_x(self):
        print(self.key)
        return self.finger * self.width

    def finger(self):
        for sub in finger:
            for i in sub:
                if i == self.key:
                    return finger.index(sub)

    def waitsibling(self):
        wait = Timer(0.2, self.siblingpass())
        wait.start()

    def siblingpass(self):
        self.nosibling = True