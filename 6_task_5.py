# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
# (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
# Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен
# выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого
# экземпляра.

class Stationery:
    def __init__(self, title):
        # атрибуты объекта
        self.title = title

    # метод
    def draw(self):
        print(f'Запуск отрисоки {self.title}')

class Pen(Stationery):

    def draw(self):
        print(f'Запуск отрисоки {self.title}. Происходит отрисовка ручкой')

class Pencil(Stationery):

    def draw(self):
        print(f'Запуск отрисоки {self.title}. Происходит отрисовка ручкой')

class Handle(Stationery):

    def draw(self):
        print(f'Запуск отрисоки {self.title}. Происходит отрисовка маркером')

pen = Pen('ручка')
pencil = Pencil('карандаш')
handle = Handle('маркер')

pen.draw()
pencil.draw()
handle.draw()

