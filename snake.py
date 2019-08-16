import pygame

class Snake:
	def __init__(self):
		self.head = [45, 45] # начальные кординаты головы змеи
		self.body = [[45, 45], [34, 45], [23, 45]] # 34 потому что убавляем координату х на 11 для того, чтобы сигментами змеи был пропуск в 1 пиксель
		self.Color = "Green" #цвет змеи
		self.points = 0

	def moove(self, control):
		"""Движение змеи в зависимости от направления (11 - так как сегмент занимает 10 и 1 пиксель на пропуск"""
		if control == "RIGHT":  # если направление направо
			self.head[0] += 11 # то прибавляем 25 к координате х
		elif control == "LEFT": # если направление влево
			self.head[0] -= 11 # то отнимаем 25 от координаты х
		elif control == "UP": # если направление вверх
			self.head[1] -= 11 # то прибавляем 25 к координате y
		elif control == "DOWN": # если направление вниз
			self.head[1] += 11 # то отнимаем 25 от координаты y
	

	def animation(self):
		"""Добавляем в начало списка голову, а хвост удаляем"""
		self.body.insert(0, list(self.head)) # указываем на какой элемент мы будем прибавлять(прибавляем голову)
		self.body.pop() # по умолчанию удаляем последний элемент списка
	
	def draw_snake(self, window):
		"""Отрисовка змеи на экране"""
		for segmnent in self.body:
			pygame.draw.rect(window, pygame.Color(self.Color), pygame.Rect(segmnent[0], segmnent[1], 10, 10)) # прорисовка головы в виде квардрата с координатами головы(head) с размером квадрата 10х10

	def check_end_window(self):
		"""Отслеживает достижение змеёй края экрана"""
		if self.head[0] == 419:   # если змея пошла направо
			self.head[0] = 23     # голове присваиваем значение 23
		elif self.head[0] == 12:  # если змея пошла налево
			self.head[0] = 419    # голове присваиваем значение 419
		elif self.head[1] == 23:  # если змея пошла наверх
			self.head[1] = 419    # голове присваиваем значение 419
		elif self.head[1] == 419: # если змея пошла вниз
			self.head[1] = 34     # голове присваиваем значение 34

	def eat(self, food, gui):
		"""Змея есть еду"""
		if self.head == food.food_position: #если координаты головы совпадает с едой
			self.body.append(food.food_position) # то к телу змеи прибавляем ещё один сигмент
			gui.get_new_indicator()
			#self.points += 1
			return True
		return False		

	def check_barrier(self, gui):
		"""Проверяет не врезалась ли змея"""
		if self.head in gui.barrier: # если голова змеи сталкивается со стеной или барьером
			self.body.pop() # то удаляем сегмент
			gui.indicator.pop() # и удаляем сегмент для индикатора конца игры
		if self.head in self.body[1:]: # если змея встречается с телом змеи
			self.body.pop()	# то удаляем сегмент тела змеи
			gui.indicator.pop() # и удаляем сегмент для индикатора конца игры