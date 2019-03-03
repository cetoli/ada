# ada.julia.main.py
from _spy.vitollino.main import Cena, Elemento, STYLE, Codigo
from math import sqrt
from random import randint
from statistics import average
from browser import timer
IMGSIZE = "240px"
W, H = 800, 600
class Sprite(Elemento):
    def __init__(self, x, y, image, cena, index=0):
        super().__init__(image, cena=cena, style=dict(left=x,top=x,width="80px",height="80px",overflow="hidden"))
        style = dict(position="relative",left=f"-{index%3*80}px",top=f"-{index//3*80}px", width=IMGSIZE, height=IMGSIZE)
        style.update({"max-width": IMGSIZE, "max-height": IMGSIZE})
        self.img.style=style
        

class Button(Sprite):
    BUTTONS = []
    DISTANCES = {}
    SHOW = Codigo("oi", style=dict(left=0, top=560, width=W))
    def __init__(self, x, y, image, cena, index=0):
        super().__init__(x, y, image, cena, index)
        self.x, self.y, self.image, self.cena, self.index = x, y, image, cena, index
        self.grav, self.ele= 10, 10
        self.heat = H//2
        self.fit = 100**10
        #timer.set_timeout(self.move, 10)
        timer.set_timeout(self.anneal, 10)
    def _move(self):
        self.x, self.y = self.x+ randint(-10,10), self.y+ randint(-10,10)
        self.elt.style.left, self.elt.style.top = self.x, self.y
        if 0< self.x < 700 and 0< self.y < 500:
            timer.set_timeout(self.move, 10)
    def do_move(self, dx, dy):
        self.x += int(dx)%W
        self.y += int(dy)%H
        self.elt.style.left, self.elt.style.top = self.x, self.y
    def move(self):
        forces = zip(*[b.force(self.x, self.y, self) for b in Button.BUTTONS if b != self])
        dx, dy = [sum(force) for force in forces]
        self.x += int(dx)
        self.y += int(dy)
        # Button.SHOW._code.text = f"{dx} {dy} {self.x} {self.y}"
        self.elt.style.left, self.elt.style.top = self.x, self.y
        if abs(dx) > 1 or abs(dy) > 1:
            timer.set_timeout(self.move, 2)
    def anneal(self):
        [b.do_move(randit(-self.heat, self.heat),randit(-self.heat, self.heat)) for b in self.BUTTONS]
        fit = self.fitness()
        self.fit, deltafit = fit, self.fit - fit
        if deltafit > 0.1
            self.heat /= 2
            timer.set_timeout(self.anneal, 1000)
            
    def fitness(self, x, y):
        distances = self.distances()
        push = average(distance for distance in distances if  distance < 90)
        pull = average(distance for distance in distances if  distance > 90)
        upull = average(distances)
        return push/pull
        '''
        ux, uy = x-W/4, y-H/2
        distance = sqrt(dx*dx + dy*dy)
        univer = sqrt(ux*ux + uy*uy )
        pull = 0.001 / min(0.1, distance) if distance > 90 else 0.0
        push = min(100, 0.1 / min(0.1, distance)) if distance < 90 else 0.0
        upull = min(0.05, 0.01 / min(0.1, univer)) if univer > 160 else 0.0
        return (-dx * pull + dx * push -ux * upull, -dy * pull + dy * push -uy * upull)'''
            
    def force(self, x, y, other):
        dx, dy = x - self.x, y - self.y
        ux, uy = x-W/3, y-H/2
        distance = sqrt(dx*dx + dy*dy)
        univer = sqrt(ux*ux + uy*uy )
        pull = 0.001 / min(0.1, distance) if distance > 100 else 0.0
        push = min(40, 0.03 / min(0.1, distance**2)) if distance < 90 else 0.0
        upull = min(0.05, 0.01 / min(0.1, univer)) if univer > 160 else 0.0
        other.do_move(dx * push, dy * push)
        return (-dx * pull -ux * upull, -dy * pull -uy * upull)
        
    def distances(self):
        return {key: value() for key, value in Button.DISTANCES.items()} 
        
    def create(self):
        Button.BUTTONS = [Button(randint(0, 800), randint(0, 300), self.image, self.cena, index) for index in range(9)]
        Button.DISTANCES = {(a, b): lambda: sqrt(a*a + b*b) for a in self.BUTTONS for b in self.BUTTONS if a != b}
        [Button.DISTANCES.pop((a, b)) for a in Button.DISTANCES for b in self.BUTTONS if (b, a) in self.DISTANCES]
        return Button.BUTTONS

class Project:
    def __init__(self):
        STYLE["width"] = 800
        STYLE["height"] = "600px"
        Buttons = "https://i.imgur.com/v6JS64Y.png"
        ARENA = "https://i.imgur.com/nS8Tas9.jpg"
        cena = Cena(ARENA)
        Button.SHOW.entra(cena)
        b0 = Button(10, 10, Buttons, cena, 0).create()
        #b0.entra(cena)
        cena.vai()


if __name__ == "__main__":
    _ = Project()