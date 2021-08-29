# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула(куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        # атрибуты объекта
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # методы
    def go(self):
        print(f'{self.name} начала движение')

    def stop(self):
        print(f'{self.name} закончила движение')

    def turn(self, i):
        print(f'{self.name} повернула на{i}')

    def show_speed(self):
        print(f'{self.name} двигается со скоростью {self.speed} км/ч')

class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'Превышение скорости автомобиля {self.name}! Немедленно сбросьте скорость до разрешённой!')
        print(f'{self.name} двигается со скоростью {self.speed} км/ч')

class SportCar(Car):
    """SportCar"""

class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print(f'Превышение скорости автомобиля {self.name}! Немедленно сбросьте скорость до разрешённой!')
        print(f'{self.name} двигается со скоростью {self.speed} км/ч')

class PoliceCar(Car):
    """PoliceCar"""

tc_1 = TownCar(60, 'Чёрная', 'KIA RIO', False)
tc_2 = TownCar(90, 'Синяя', 'KIA OPTIMA', False)

tc_1.go()
tc_2.go()
tc_1.turn('право')
tc_1.show_speed()
tc_2.show_speed()
tc_1.stop()
tc_2.stop()




