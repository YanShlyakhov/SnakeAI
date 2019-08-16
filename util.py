import pygame
import pygame.font


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (50, 50, 255)
GREY = (200, 200, 200)
ORANGE = (200, 100, 50)
TRANS = (1, 1, 1)
GREEN = (0, 255, 0)

class Button():
    def __init__(self, ai_settings, screen, msg, x ,y, width, height):
        # инициализирует атрибуты кнопки
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.msg = msg

        #назначение размеров и свойств кнопок
        self.width, self.height = width, height#200, 50
        self.button_color = ai_settings.current_color
        #self.text_color = (255, 255, 255)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont("comicsansms", 30)

        #построение объекта rect кнопки и выравнивание его по центру экрана
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)#self.screen_rect.center

        #сообщение кнопки созхдаётся только один раз
        self.prep_msg(msg, ai_settings)

    def prep_msg(self, msg, ai_settings):
        #преобразует msg в прямоугольник и выравнивает текст по центру
        self.msg_image = self.font.render(msg, True, self.text_color, ai_settings.current_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self, ai_settings):
        #отображение пустой кнопки и вывод сообщения
        self.screen.fill(ai_settings.current_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)



