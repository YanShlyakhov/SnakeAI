import pygame
from collection import Settings
from pygame.sprite import Group
import os
import sys
from util import Button
from main import play

def run_game():

    #инициализируем игру и создаём объект экрана
    pygame.init()
    settings = Settings()
    background_image = settings.gui_image

    #перемещаем окно
    os.environ['SDL_VIDEO_WINDOW_POS'] = '{},{}'.format(500, 150)
    screen = pygame.display.set_mode((441, 480))
    pygame.display.set_caption("Змейка")

    #создание кнопки Play
    play_button = Button(settings, screen, "Play", 441 / 2,  441 / 2-30, 200, 50)
    butt_exit = Button(settings, screen, "Exit", 441 / 2, 441 / 2 + 70, 200, 50)

    buttons = [play_button, butt_exit]

    #запуск основного цикла игры
    while True:
        check_events(buttons)
        screen.blit(background_image, (0, 0))

        for button in buttons:
            button.draw_button(settings)

        pygame.display.flip()
        settings.clock.tick(30)

def check_events(buttons):
    #обрабатывает нажатия клавиш и события мыши
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(buttons[0], mouse_x, mouse_y)
            check_exit_button(buttons[1], mouse_x, mouse_y)

def check_play_button(play_button, mouse_x, mouse_y):
    #запускает новую игру при нажатии кнопки Play
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked:
        #sound of clicking on button
        play()

def check_exit_button( button, mouse_x, mouse_y):
    button_clicked = button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked:
        #sound of clicking on button
        sys.exit()

run_game()