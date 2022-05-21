import pygame
from src.c2d.components.GameComponent import GameComponent
from src.c2d.game_object import GameObject


class FollowMouse(GameComponent):
    def __init__(self, offset: tuple=(0,0)):
        super().__init__()
        self.offset = offset
    
    def start(self, game_object: GameObject):
        super().start(game_object=game_object)
    
    def update(self, game_object: GameObject):
        super().update(game_object=game_object)
        m_pos = pygame.mouse.get_pos()
        game_object.set_pos((m_pos[0]+self.offset[0], m_pos[1]+self.offset[1]))