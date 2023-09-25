import random

# Создаем интерфейсы IMove и IHealth
class IMove:
    def move(self, direction):
        pass

class IHealth:
    def __init__(self):
        self.health = 100

# Создаем классы для различных типов самолетов
class Aircraft(IMove, IHealth):
    def __init__(self, x, y, symbol):
        super().__init__()
        self.x = x
        self.y = y
        self.symbol = symbol

    def move(self, direction):
        if direction == "up" and self.y > 0:
            self.y -= 1
        elif direction == "down" and self.y < 9:
            self.y += 1
        elif direction == "left" and self.x > 0:
            self.x -= 1
        elif direction == "right" and self.x < 9:
            self.x += 1

class Fighter(Aircraft):
    def attack(self, target):
        if isinstance(target, Aircraft):
            print(f"{self.symbol} истребил {target.symbol}")
            target.health = 0

class Bomber(Aircraft):
    def attack(self, target):
        if isinstance(target, Base):
            print(f"{self.symbol} бомбардировал базу")
            target.health = 0

class Scout(Aircraft):
    def __init__(self, x, y):
        super().__init__(x, y, "S")

    def buff(self, target):
        if isinstance(target, Aircraft):
            print(f"{self.symbol} дал бафф {target.symbol}")

class Base(IHealth):
    def __init__(self):
        super().__init__()
        self.symbol = "B"

# Создаем карту и размещаем объекты
map_size = 10
map = [['.' for _ in range(map_size)] for _ in range(map_size)]

fighter1 = Fighter(0, 0, "F")
fighter2 = Fighter(9, 9, "F")
bomber = Bomber(3, 3)
scout = Scout(5, 5)
base = Base()

map[fighter1.y][fighter1.x] = fighter1.symbol
map[fighter2.y][fighter2.x] = fighter2.symbol
map[bomber.y][bomber.x] = bomber.symbol
map[scout.y][scout.x] = scout.symbol
map[base.y][base.x] = base.symbol

# Функция для отображения карты
def display_map():
    for row in map:
        print(" ".join(row))

# Функция для проверки победы
def check_victory():
    if base.health <= 0:
        print("База уничтожена! Игра окончена.")
        return True
    return False

# Главный игровой цикл
current_player = 1
victory = False

while not victory:
    display_map()
    print(f"Игрок {current_player}, ваш ход:")
    x, y = -1, -1
    while x < 0 or x >= map_size or y < 0 or y >= map_size:
        x = int(input("Введите X координату: "))
        y = int(input("Введите Y координату: "))

    selected_aircraft = None
    if map[y][x] == fighter1.symbol:
        selected_aircraft = fighter1
    elif map[y][x] == fighter2.symbol:
        selected_aircraft = fighter2
    elif map[y][x] == bomber.symbol:
        selected_aircraft = bomber
    elif map[y][x] == scout.symbol:
        selected_aircraft = scout

    if selected_aircraft:
        print(f"Выбран {selected_aircraft.symbol}")
        action = input("Выберите действие (move/attack/buff): ")
        if action == "move":
            direction = input("Выберите направление (up/down/left/right): ")
            selected_aircraft.move(direction)
        elif action == "attack":
            x_target = int(input("Введите X координату цели: "))
            y_target = int(input("Введите Y координату цели: "))
            if x_target == base.x and y_target == base.y:
                selected_aircraft.attack(base)
            elif map[y_target][x_target] == fighter1.symbol:
                selected_aircraft.attack(fighter1)
            elif map[y_target][x_target] == fighter2.symbol:
                selected_aircraft.attack(fighter2)
        elif action == "buff":
            x_target = int(input("Введите X координату цели: "))
            y_target = int(input("Введите Y координату цели: "))
            target = None
            if map[y_target][x_target] == fighter1.symbol:
                target = fighter1
            elif map[y_target][x_target] == fighter2.symbol:
                target = fighter2
            if target:
                scout.buff(target)

        map = [['.' for _ in range(map_size)] for _ in range(map_size)]
        map[fighter1.y][fighter1.x] = fighter1.symbol
        map[fighter2.y][fighter2.x] = fighter2.symbol
        map[bomber.y][bomber.x] = bomber.symbol
        map[scout.y][scout.x] = scout.symbol
        map[base.y][base.x] = base.symbol

        current_player = 3 - current_player  # Переключение между игроками

    victory = check_victory()
