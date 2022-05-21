from random import randrange
from src.c2d.Game import Game
import pygame


class GameObject:
    def __init__(self, x: int=0, y: int=0, components: list=[]):
        self.components = components
        self.color = (255,255,255)
        self.x = x
        self.y = y

    def start(self, game: Game):
        for component in self.components:
            component.start(self)
    
    def update(self, game):
        for component in self.components:
            component.update(self)
    
    def draw(self, game):
        ...
    
    def set_pos(self, pos: tuple):
        self.x = pos[0]
        self.y = pos[1]

class Rectangle(GameObject):
    def __init__(self, w, h, x, y, components: list=[]):
        super().__init__(x, y, components)
        self.w = w
        self.h = h

class Circle(GameObject):
    def __init__(self, r, x, y, components: list=[]):
        super().__init__(x, y, components)
        self.r = r

    def draw(self, game):
        super().draw(game)
        pygame.draw.circle(game.screen, self.color, (self.x, self.y), self.r)

class Box(Rectangle):
    def __init__(self, s: int, x: int, y: int, components: list=[]):
        super().__init__(s, s, x, y, components)
        self.color = (randrange(1, 255), randrange(1, 255), randrange(1, 255))
    
    def draw(self, game):
        super().draw(game)
        pygame.draw.rect(game.screen, self.color, (self.x, self.y, self.w, self.h))