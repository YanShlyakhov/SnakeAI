import pygame
from pygame.locals import *

class Control:
		def __init__(self):
			self.flag_game = True
			self.flag_direction = "RIGHT" # флаг направления движения
			self.flag_pause = True # флаг паузы

		def control(self):
			"""Управление в зависимости от флага"""
			for event in pygame.event.get():
				if event.type == QUIT: # если нажать "крестик", то закроется окно
					self.flag_game = False
				elif event.type == KEYDOWN: # означает, что кнопка нажата
					if event.key == K_RIGHT and self.flag_direction != "LEFT": # если нажали стрелку ->
						self.flag_direction = "RIGHT" # задаём направление направо
					elif event.key == K_LEFT and self.flag_direction != "RIGHT": # если нажали стрелку <-
						self.flag_direction = "LEFT" # задаём направление влево
					elif event.key == K_UP and self.flag_direction != "DOWN": # если нажали стрелку вверх
						self.flag_direction = "UP" # задаём направление вверх
					elif event.key == K_DOWN and self.flag_direction != "UP": # если нажали стрелку вниз
						self.flag_direction = "DOWN" # задаём направление вниз
					elif event.key == K_ESCAPE: # ecли нажали клавишу ESC, то выходим из программы
						self.flag_game = False # flag_game - флаг для основного цикла
					elif event.key == K_SPACE: # если нажали SPACE, то игра останавливается/продолжается
						if self.flag_pause:
							self.flag_pause = False
						elif self.flag_pause == False:
							self.flag_pause = True