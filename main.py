from src.c2d.Game import Game
from src.c2d.components.collider_engine import ColliderEngine
from src.c2d.game_object import Box, Circle
from src.c2d.components.FollowMouse import FollowMouse
from src.c2d.components.collider import CircleCollider, RectangleCollider

def main():
    screen_size=(500,500)
    collider_engine = ColliderEngine()
    game_objects = [
        Box(100, screen_size[0]/2-50, screen_size[1]/2-50, [RectangleCollider(collider_engine, 100, 100)]),
        Box(100, screen_size[0]/2-50, screen_size[1]/2-50, [RectangleCollider(collider_engine, 100, 100), FollowMouse()]),
        #Circle(30, 300, 300, [CircleCollider(collider_engine, 30)]),
        #Circle(30, 300, 300, [FollowMouse(),CircleCollider(collider_engine, 30)])
    ]
    game = Game(screen_size=screen_size, target_fps=60, game_objects=game_objects, engines=[collider_engine])
    game.start()


main()