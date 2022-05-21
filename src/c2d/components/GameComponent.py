from src.c2d.game_object import GameObject


class GameComponent:
    def __init__(self):
        ...
    
    def start(self, game_object: GameObject):
        self.game_object = game_object

    def update(self, game_object: GameObject):
        ...
