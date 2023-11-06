import random

class CafeSimulation:
    def __init__(self, num_tables, num_waiters, simulation_hours):
        self.num_tables = num_tables
        self.num_waiters = num_waiters
        self.simulation_hours = simulation_hours
        self.tables = [True] * num_tables  # True означає вільний столик
        self.waiters = [True] * num_waiters  # True означає вільного офіціанта

    def simulate(self):
        total_customers = 0
        served_customers = 0
        for hour in range(self.simulation_hours):
            # Генерація кількості клієнтів, які приходять у дану годину (приклад)
            customers = random.randint(1, 10)
            total_customers += customers
            
            # Обслуговування клієнтів
            for _ in range(customers):
                table = self._find_free_table()
                waiter = self._find_free_waiter()
                if table is not None and waiter is not None:
                    served_customers += 1
                    self.tables[table] = False
                    self.waiters[waiter] = False
                    
            # Моделювання часу, який клієнти проводять в кафе (приклад)
            serving_time = random.randint(15, 60)  # час в хвилинах
            # Вивільнення столиків та офіціантів після закінчення обслуговування
            for i in range(self.num_tables):
                if not self.tables[i]:
                    serving_time -= 1
                    if serving_time <= 0:
                        self.tables[i] = True
            for i in range(self.num_waiters):
                if not self.waiters[i]:
                    serving_time -= 1
                    if serving_time <= 0:
                        self.waiters[i] = True
        
        # Результати симуляції
        print(f"Загальна кількість клієнтів: {total_customers}")
        print(f"Кількість обслугованих клієнтів: {served_customers}")
        print(f"Відсоток обслугованих клієнтів: {served_customers / total_customers * 100:.2f}%")

    def _find_free_table(self):
        for i in range(self.num_tables):
            if self.tables[i]:
                return i
        return None

    def _find_free_waiter(self):
        for i in range(self.num_waiters):
            if self.waiters[i]:
                return i
        return None

# Приклад використання симуляції
num_tables = 10  # Кількість столиків у кафе
num_waiters = 3  # Кількість офіціантів у кафе
simulation_hours = 12  # Тривалість симуляції у годинах

cafe_simulation = CafeSimulation(num_tables, num_waiters, simulation_hours)
cafe_simulation.simulate()
