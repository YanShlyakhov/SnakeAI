import pygame
import random

class Food:
	def __init__(self):
		self.food_position = [] # список для хранения координат нашей еды
		self.timer = 100

	def get_food_position(self, gui, body1, body2):
		"""
			Выдаёт рандомное значение координат еды
			не вставляет еду внутри змей
		"""
		free_field = gui.field
		for i in body1:
			if free_field.count(i) > 0:
				free_field.remove(i)

		for i in body2:
			if free_field.count(i) > 0:
				free_field.remove(i)

		self.food_position = random.choice(free_field) # choice - метод, выдающий рандомное значение из списка
		self.timer = 100 * 25 #время жизни еды

	def draw_food(self, window):
		"""Отрисовывает еду"""
		pygame.draw.rect(window, pygame.Color("Red"), pygame.Rect(self.food_position[0], self.food_position[1], 10, 10))
		self.timer -=1
		
		
		