import typing
import pygame

class Page:
    def __init__(self, screen, height, width, scale, fonts: typing.Tuple[str, pygame.font.SysFont]) -> None:
        self.screen = screen
        self.height = height
        self.width = width
        self.scale = scale
        self.fonts = fonts