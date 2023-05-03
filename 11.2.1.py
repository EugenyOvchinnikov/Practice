# Напишите класс Toyota, состоящий из четырёх статических атрибутов:
#
#     цвет машины (например, красный),
#     цена (один миллион),
#     максимальная скорость (200),
#     текущая скорость (ноль).
#
# Создайте три экземпляра класса и каждому из них поменяйте значение текущей скорости на случайное число от нуля до 200.
import random


class Toyota:
    color = 'red'
    cost = 1e6
    max_speed = 200
    current_speed = 0


rav4 = Toyota()
rav4.current_speed = random.randint(0, 200)

corolla = Toyota()
corolla.current_speed = random.randint(0, 200)

landcruiser = Toyota()
landcruiser.current_speed = random.randint(0, 200)

print(rav4.cost)
