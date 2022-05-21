from src.c2d.components.GameComponent import GameComponent
from src.c2d.game_object import GameObject

class Collider(GameComponent):
    def __init__(self, engine):
        self.engine = engine
        self.is_colliding = False
        self.is_started = False
    
    def start(self, game_object: GameObject):
        self.engine.add_collider(self)
        self.is_started = True

    def on_destroy(self):
        self.engine.remove_collider(self)
    
    def update(self, game_object: GameObject):
        if (not self.is_started):
            raise Exception()
    
    def update_physics(self, game_object: GameObject):
        if (not self.is_started):
            raise Exception()

class CircleCollider(Collider):
    def __init__(self, engine, r):
        super().__init__(engine)
        self.r = r
    
    def start(self, game_object: GameObject):
        super().start(game_object=game_object)
        self.game_object = game_object

class RectangleCollider(Collider):
    def __init__(self, engine, w, h):
        super().__init__(engine)
        self.w = w
        self.h = h
    
    def start(self, game_object: GameObject):
        super().start(game_object=game_object)
        self.game_object = game_object