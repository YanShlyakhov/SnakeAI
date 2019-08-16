import pygame
class Settings:
    def __init__(self):
        self.current_color = (255, 0, 0)
        self.gui_image = pygame.image.load("images/snake_test.png")
        self.clock = pygame.time.Clock()