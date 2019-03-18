# ada.julia.main.py
from _spy.vitollino.main import Cena, Elemento, STYLE, Codigo
from math import sqrt
from random import randint
from browser import timer

IMGSIZE = "240px"
W, H = 800, 540


class Sprite(Elemento):
    def __init__(self, x, y, image, cena, index=0):
        super().__init__(image, cena=cena,
                         style=dict(left=x, top=y, width="80px", height="80px", overflow="hidden"))
        style = dict(position="relative", left=f"-{index % 3 * 80}px",
                     top=f"-{index // 3 * 80}px", width=IMGSIZE, height=IMGSIZE)
        style.update({"max-width": IMGSIZE, "max-height": IMGSIZE})
        self.img.style = style


class Button(Sprite):
    BUTTONS = []
    DISTANCES = {}
    XYDISTANCES = {}
    SHOW = Codigo("oi", style=dict(left=0, top=560, width=W))

    def __init__(self, x, y, image, cena, index=0):
        super().__init__(x, y, image, cena, index)
        self.x, self.y, self.image, self.cena, self.index = x, y, image, cena, index
        self.grav, self.ele = 10, 10
        self.heat = H // 2
        self.fit = 10000000
        # timer.set_timeout(self.move, 10)
        # timer.set_timeout(self.anneal, 10)

    def _move(self):
        self.x, self.y = self.x + randint(-10, 10), self.y + randint(-10, 10)
        self.elt.style.left, self.elt.style.top = self.x, self.y
        if 0 < self.x < 700 and 0 < self.y < 500:
            timer.set_timeout(self.move, 10)

    def __do_move(self, dx, dy):
        self.x = (self.x + int(dx)) % W
        self.y = (self.y + int(dy)) % H
        self.elt.style.left, self.elt.style.top = self.x, self.y
        return self.x, self.y

    def move(self, *_):
        distances_to_here = [distance(c=-1) if self == key[0] else distance()
                             for key, distance in self.XYDISTANCES.items() if self in key]
        # forces = zip(*[b.force(self.x, self.y, self) for b in Button.BUTTONS if b != self])
        dx, dy = [sum(force) for force in zip(*distances_to_here)]
        self.x += int(dx)
        self.y += int(dy)
        # Button.SHOW._code.text = f"{dx} {dy} {self.x} {self.y}"
        self.elt.style.left, self.elt.style.top = self.x, self.y
        # if abs(dx) > 1 or abs(dy) > 1:
        #     timer.set_timeout(self.move, 2)
        return len(distances_to_here)  # self.x, self.y

    def anneal(self):
        Button.SHOW._code.text = "anneal"
        heat = int(self.heat)
        moves = [b.move() for b in self.BUTTONS]
        Button.SHOW._code.text = f"b.do_move {moves}"
        fit = self.fitness()
        self.fit, deltafit = fit, self.fit - fit + 1
        # Button.SHOW._code.text = f"self.fitt:{self.fit}, the fit::{fit}, deltafiti:{deltafit}"
        if abs(deltafit) > 0.0001:
            self.heat = self.heat * 0.78 if deltafit < 0 else self.heat * 1.2
            # Button.SHOW._code.text = f"self.heat = {self.heat} fited:{fit}, deltafitd:{deltafit}"
            timer.set_timeout(self.anneal, 100)

    def fitness(self):
        def mean(values):
            values = list(values)
            return sum(values) / (len(values) if values else 1)

        distances = self.distances()
        # Button.SHOW._code.text = f"fitness: {mean(list(distances))}"
        push = mean([distance for distance in distances if distance < 90]) + 1
        pull = [distance for distance in distances if distance > 90]
        upull = min(0.5, mean(distances))
        # Button.SHOW._code.text = f"push:{push},pull:{pull}fit: {list(distances)}"
        return push * (mean(pull) + 1) * upull * (sum(pull) + 1)

    def __force(self, x, y, other):
        dx, dy = x - self.x, y - self.y
        ux, uy = x - W / 3, y - H / 2
        distance = sqrt(dx * dx + dy * dy)
        univer = sqrt(ux * ux + uy * uy)
        pull = 0.001 / min(0.1, distance) if distance > 100 else 0.0
        push = min(40, 0.03 / min(0.1, distance ** 2)) if distance < 90 else 0.0
        upull = min(0.05, 0.01 / min(0.1, univer)) if univer > 160 else 0.0
        other.do_move(dx * push, dy * push)
        return (-dx * pull - ux * upull, -dy * pull - uy * upull)

    def distances(self):
        def distance(a, b):
            dx, dy = a.x - b.x, a.y - b.y
            return sqrt(dx * dx + dy * dy)

        return [distance(a, b) for a, b in Button.DISTANCES.keys()]
        # return {key: value() for key, value in Button.DISTANCES.items()}

    def create(self):

        def xydistance(i, j, k=1):
            return (i.x - j.x)*k, (i.y - j.y)*k

        def distance(a, b):
            dx, dy = a.x - b.x, a.y - b.y
            return sqrt(dx * dx + dy * dy)

        Button.BUTTONS = [Button(randint(0, 800), randint(0, 300), self.image, self.cena, index) for index in range(9)]
        # Button.DISTANCES = {(a, b): lambda: distance(a, b) for a in self.BUTTONS for b in self.BUTTONS if a != b}
        for a in self.BUTTONS:
            for b in self.BUTTONS:
                if a != b and (b, a) not in Button.DISTANCES:
                    Button.DISTANCES[(a, b)] = lambda: distance(a, b)
                    Button.XYDISTANCES[(a, b)] = lambda c=1: xydistance(a, b, c)
        # Button.DISTANCES = {(a, b): lambda: distance(a, b) for a in self.BUTTONS for b in self.BUTTONS if a != b}
        # [Button.DISTANCES.pop((b, a)) for a, b in Button.DISTANCES.keys() if (b, a) in self.DISTANCES]
        Button.SHOW._code.text = str(len(self.distances()))
        timer.set_timeout(self.anneal, 1000)
        return Button.BUTTONS


class Project:
    def __init__(self):
        STYLE["width"] = 800
        STYLE["height"] = "600px"
        Buttons = "https://i.imgur.com/v6JS64Y.png"
        ARENA = "https://i.imgur.com/nS8Tas9.jpg"
        cena = Cena(ARENA)
        Button.SHOW.entra(cena)
        _ = Button(10, 10, Buttons, cena, 0).create()
        cena.vai()


def main():
    _ = Project()


if __name__ == "__main__":
    main()
