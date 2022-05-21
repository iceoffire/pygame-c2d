from collections.abc import Callable
import pygame
from pygame.locals import *
from utils import fps

class Game:
    def __init__(self, screen_size: tuple, target_fps, game_objects: list, engines: list, on_exit: Callable=None):
        self.is_running = True
        self.screen_size = screen_size
        self.game_objects = game_objects
        self.target_fps = target_fps
        self.screen = pygame.display.set_mode(screen_size)
        self.exit_request = False
        self.engines = engines
        pass

    def start(self):
        for engine in self.engines:
            engine.start(self)
        for game_object in self.game_objects:
            game_object.start(self)
        while self.is_running:
            self.update()
            self.draw()

    def update(self):
        self.__check_exit()
        self.__update_engines()
        self.__update_game_objects()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.__draw_game_objects()
        pygame.display.flip()
        fps(self.target_fps)

    def exit(self):
        pygame.quit()

    def __check_exit(self):
        for e in pygame.event.get():
            if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
                self.is_running = False
        pass

    def __update_game_objects(self):
        for game_object in self.game_objects:
            game_object.update(self)

    def __update_engines(self):
        for engine in self.engines:
            engine.update(self)

    def __draw_game_objects(self):
        for game_object in self.game_objects:
            game_object.draw(self)