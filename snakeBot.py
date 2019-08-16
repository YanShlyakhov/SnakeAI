from snake import Snake

#константа на расстояние до клетки(просто большое значение, которое недостижимо)
NO_USE = 99999

#наследуемся от класса Snake, чтобы не переписывать основные методы
class Bot(Snake):
    
    level_map = [[0 for i in range(45)] for j in range(45)]
    dist_map = [[NO_USE for i in range(45)] for j in range(45)]
    apple_pos = [0, 0]
    head_normal = [4, 4]

    route = []

    def __init__(self):
        self.head = [45, 45]
        self.body = [[45, 56], [34, 56], [23, 56]] 
        self.Color = "Pink"

    def eat(self, food, gui):
		
        if self.head == food.food_position: 
            self.body.append(food.food_position) 
            gui.indicator.pop()
            return True
        return False

    """
        проверяем клетку, если не голова, то ищем вокруг клетку с расстоянием на единицу меньше
    """
    def make_route(self, position):
        _dx = [0, 0, 1, -1]
        _dy = [1, -1, 0, 0]
        dst = self.dist_map[position[1]][position[0]]
        if(dst == 0):
            return

        for i in range(4):
            cur_x = position[0] + _dx[i]
            cur_y = position[1] + _dy[i]
            if(self.dist_map[cur_y][cur_x] + 1 == dst):
                self.route.append([cur_x, cur_y])
                self.make_route([cur_x, cur_y])
                break
        return 

    """
        создаем матрицу размера карты, где каждая клетка показывает расстояние 
        от головы до яблока
    """
    def bfs(self):
        #куда мы можем динуться 
        _dx = [0, 0, 1, -1]
        _dy = [1, -1, 0, 0]

        global NO_USE

        #очередь
        queue = []
        queue.append(self.head_normal)
        #матрица расстояний
        self.dist_map = [[NO_USE for i in range(40)] for j in range(40)]
        self.dist_map[self.head_normal[1]][self.head_normal[0]] = 1

        #пока очередь не пуста, то будем рассматривать все клетки вокруг
        while len(queue) != 0:
            cur = queue[0]
            queue.pop(0)
            dst = self.dist_map[cur[1]][cur[0]]
            for i in range(4):
                cur_x = cur[0] + _dx[i]
                cur_y = cur[1] + _dy[i]
                #берем одну из клеток вокруг и проверям; а можем ли мы в нее попасть?
                if(cur_x > 0 and cur_x <40 and cur_y > 0 and cur_y<40):
                    if(self.level_map[cur_y][cur_x] == 1 and self.dist_map[cur_y][cur_x] == NO_USE):
                        self.dist_map[cur_y][cur_x] = dst + 1
                        queue.append([cur_x, cur_y])
        
        #строим путь от яблока до головы, рекурсивно 
        self.route = []
        self.route.append(self.apple_pos)
        self.make_route(self.apple_pos)
        print(len(self.route))
        #print(self.route)
        self.route.reverse()
        #если следующая клетка яблоко, то едем по той же траектории
        if(len(self.route) == 1):
            return
        
        #рассматриваем две координаты
        p1 = self.route[0]
        p2 = self.route[1]

        
        # 1 -- Y, 0 -- X, куда нам надо повернуть?
        #рассмотрим 4 случая
        if(p1[1] + 1 == p2[1]):
            return "DOWN"
        if(p1[1] - 1 == p2[1]):
            return "UP"
        if(p1[0] + 1 == p2[0]):
            return "RIGHT"
        if(p1[0] - 1 == p2[0]):
            return "LEFT"


    """
        на вход: положение яблока и карта
        на выход: куда стоит повернуть
    """
    def move(self, apple_pos, level_map):
        x = 0
        y = 0
        #создание карты на основы одномерного массива
        for i in level_map:
            self.level_map[y+1][x+1] = i
            x+=1
            if(x == 40):
                x = 0
                y += 1
        
        #добавление тела змеи
        for p in self.body:
            x = int((p[0] + 10) / 11)
            y = int((p[1] + 10) / 11)
            self.level_map[y][x] = 0
        #если яблоко находится где-то в недосяаемом месте, то говорим змее ползти в центр
        try:
            self.apple_pos[0] = int((apple_pos[0] + 10) / 11) 
            self.apple_pos[1] = int((apple_pos[1] + 10) / 11)  
        except:
            self.apple_pos[0] = 20
            self.apple_pos[1] = 20
        
        #позиция головы
        self.head_normal[0] = int((self.head[0] + 10) / 11)
        self.head_normal[1] = int((self.head[1] + 10) / 11)

        #запускаем алгоритм поиска в ширину
        return self.bfs()
    