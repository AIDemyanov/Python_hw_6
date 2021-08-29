# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе
# Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
# (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать
# данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        # атрибуты объекта
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):

    def get_full_name(self):
        return f'Полное имя сотрудника - {self.surname} {self.name}'

    def get_total_income(self):
        return sum(self._income.values())

position_a = Position('Иван', 'Иванов', 'Аналитик', 100_000, 50_000)
print(position_a.get_full_name())
print(position_a.get_total_income())


