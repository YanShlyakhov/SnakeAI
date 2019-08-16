import pygame
from control import Control
from snake import Snake
from gui import Gui
from food import Food
from snakeBot import Bot

def play():
	pygame.init() # инициализируем библиотеку pygame
	window = pygame.display.set_mode((441, 480)) # создание окна c размером
	pygame.display.set_caption("Змейка") # задаём название окна
	control = Control()
	snake = Snake()
	bot = Bot()
	#is_basic True -- запуск обычный, False -- запуск рандомной карты из файлов
	gui = Gui(is_basic=False)
	food = Food()
	gui.init_field()
	food.get_food_position(gui, snake.body, bot.body)
	var_speed = 0 # переменная для регулировки скорости выполнения программы
	
	#gui.create_image()

	while control.flag_game:
		gui.check_win_lose(snake.body)
		control.control()
		window.fill(pygame.Color("Black")) # закрашивание предыдущего квадрата чёрным цветом
		if gui.game == "GAME": # если флаг равен "GAME"
			snake.draw_snake(window) # то вызываем метод отрисовки змеи на экране
			bot.draw_snake(window) #отрисовка бота-змеи
			if(food.timer <= 0): # проверка на жизнь еды
				food.get_food_position(gui, snake.body, bot.body)
			food.draw_food(window) # и метод отрисовки еды
		elif gui.game == "WIN":  # если флаг равен "WIN"
			if(bot.points <= snake.points): #проверка очков, кто больше набрал
				gui.draw_win(window) 
			else:
				gui.draw_lose(window)	
		elif gui.game == "LOSE": # если флаг равен "LOSE"
			gui.draw_lose(window)# то отрисовываем избражение поражения
		gui.draw_indicator(window)
		gui.draw_level(window)
		if var_speed % 50 == 0 and control.flag_pause:   # если делится без остатка, то производим изменение координаты квадрата and реакция на паузу
			snake.moove(control.flag_direction)
			snake.check_barrier(gui)
			
			mv = "" #проверка бота, все ли работает правильно (можно убрать, но так спокойнее)
			try:
				mv = bot.move(food.food_position, gui.level)
			except:
				mv = bot.move(food.food_position, gui.level)
			#print(mv)
			bot.moove(mv)
			#не трубуется, тк бот никогда к ним не подлезет bot.check_barrier(gui)
			#проверка на съедение и генерация новой еды вне тела змеи
			if snake.eat(food, gui) or bot.eat(food, gui):
				food.get_food_position(gui, snake.body, bot.body)
			
			bot.check_end_window()
			snake.check_end_window()
			bot.animation()
			snake.animation()
		var_speed += 1
		pygame.display.flip() # метод отображения окна