# Напишите класс Segment
# Для его инициализации нужно два кортежа с координатами точек (x1, y1), (x2, y2)
# Реализуйте методы класса:
# 1. length, который возвращает длину нашего отрезка, с округлением до 2 знаков после запятой
# 2. x_axis_intersection, который возвращает True, если отрезок пересекает ось абцисс, иначе False
# 3. y_axis_intersection, который возвращает True, если отрезок пересекает ось ординат, иначе False
# Например (Ввод --> Вывод) :
# Segment((2, 3), (4, 5)).length() --> 2.83
# Segment((-2, -3), (4, 5)).x_axis_intersection() --> True
# Segment((-2, -3), (-4, -5)).y_axis_intersection() --> False

# Здесь пишем код
class Segment:
    def __init__(self, tochka1, tochka2):
        self.tochka1 = tochka1  # Координаты точек первого кортежа
        self.tochka2 = tochka2  # Координаты точек второго кортежа

    def length(self):
        """
        Функция вычисляет и возвращает длину нашего отрезка.
        :return: Длина отрезка, с округлением до 2-х знаков после запятой.
        """
        x1, y1 = self.tochka1
        x2, y2 = self.tochka2
        return round((((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5), 2)

    def x_axis_intersection(self):
        """
        Функция возвращает True, если отрезок пересекает ось абцисс, иначе False
        :return: True или False
        """
        x1, y1 = self.tochka1
        x2, y2 = self.tochka2
        if y1 == 0 or y2 == 0 or y1 * y2 < 0:
            return True
        else:
            return False

    def y_axis_intersection(self):
        """
        Функция возвращает True, если отрезок пересекает ось ординат, иначе False
        :return: True или False
        """
        x1, y1 = self.tochka1
        x2, y2 = self.tochka2
        if x1 == 0 or x2 == 0 or x1 * x2 < 0:
            return True
        else:
            return False


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [Segment((2, 3), (4, 5)).length,
        Segment((1, 1), (1, 8)).length,
        Segment((0, 0), (0, 1)).length,
        Segment((15, 1), (18, 8)).length,
        Segment((-2, -3), (4, 5)).x_axis_intersection,
        Segment((-2, -3), (-4, -2)).x_axis_intersection,
        Segment((0, -3), (4, 5)).x_axis_intersection,
        Segment((2, 3), (4, 5)).y_axis_intersection,
        Segment((-2, -3), (4, 5)).y_axis_intersection,
        Segment((-2, 3), (4, 0)).y_axis_intersection
        ]

test_data = [2.83, 7.0, 1.0, 7.62, True, False, True, False, True, True]

for i, d in enumerate(data):
    assert_error = f'Не прошла проверка для метода {d.__qualname__} экземпляра с атрибутами {d.__self__.__dict__}'
    assert d() == test_data[i], assert_error
    print(f'Набор для метода {d.__qualname__} экземпляра класса с атрибутами {d.__self__.__dict__} прошёл проверку')
print('Всё ок')
