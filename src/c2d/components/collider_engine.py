from src.c2d.components.collider import CircleCollider, RectangleCollider, Collider
from src.c2d.components.GameEngine import GameEngine
from src.c2d.Game import Game


class ColliderEngine(GameEngine):
    def __init__(self):
        self.colliders = []
        self.test_colliders = {}
        self.start_test_colliders()

    def start(self, game: Game):
        super().start(game)

    def start_test_colliders(self):
        self.test_colliders[(CircleCollider, RectangleCollider)] = CircleRectangleCollision()
        self.test_colliders[(RectangleCollider, CircleCollider)] = RectangleCircleCollision()
        self.test_colliders[(CircleCollider, CircleCollider)] = CircleCircleCollision()
        self.test_colliders[(RectangleCollider, RectangleCollider)] = RectangleRectangleCollision()

    def update(self, game: Game):
        for i, collider in enumerate(self.colliders):
            for other in self.colliders[i:]:
                if (other != collider):
                    is_colliding = self.test_colliders[(type(collider), type(other))].test(collider, other)
                    if (is_colliding):
                        print(f'({(type(collider), type(other))} is colliding')

    def add_collider(self, collider: Collider):
        self.colliders.append(collider)
    
    def remove_collider(self, collider: Collider):
        self.colliders.remove(collider)

class RectangleCircleCollision:
    def __init__(self):
        ...
    
    def test(self, rc: RectangleCollider, cc: CircleCollider) -> bool:
        circle = cc.game_object
        rect = rc.game_object

        test_x = circle.x
        test_y = circle.y
        if (circle.x < rect.x):
            test_x = rect.x
        elif (circle.x > rect.x + rc.w):
            test_x = rect.x + rc.w
        
        if (circle.y < rect.y):
            test_y = rect.y
        elif (circle.y > rect.y + rc.h):
            test_y = rect.y + rc.h
        
        dist_x = circle.x-test_x
        dist_y = circle.y-test_y

        dist = (dist_x**2 + dist_y**2)**0.5
        return dist <= circle.r


class CircleRectangleCollision:
    def __init__(self):
        ...
    
    def test(self, cc: CircleCollider, rc: RectangleCollider) -> bool:
        circle = cc.game_object
        rect = rc.game_object
        test_x = circle.x
        test_y = circle.y
        if (circle.x < rect.x):
            test_x = rect.x
        elif (circle.x > rect.x + rc.w):
            test_x = rect.x + rc.w
        
        if (circle.y < rect.y):
            test_y = rect.y
        elif (circle.y > rect.y + rc.h):
            test_y = rect.y + rc.h

        dist_x = circle.x-test_x
        dist_y = circle.y-test_y

        dist = (dist_x**2 + dist_y**2)**0.5
        return dist <= circle.r

class CircleCircleCollision:
    def __init__(self):
        ...
    
    def test(self, cc1: CircleCollider, cc2: CircleCollider) -> bool:
        c1 = cc1.game_object
        c2 = cc2.game_object
        dist_x = c1.x-c2.x
        dist_y = c1.y-c2.y
        dist = (dist_x**2 + dist_y**2)**0.5
        return dist <= (cc1.r+cc2.r)

class RectangleRectangleCollision:
    def __init__(self):
        ...
    
    def test(self, rc1: RectangleCollider, rc2: RectangleCollider):
        r1 = rc1.game_object
        r2 = rc2.game_object
        return (r1.x + rc1.w >= r2.x and
            r1.x <= r2.x + rc2.w and
            r1.y + rc1.h >= r2.y and
            r1.y <= r2.y + rc2.h)