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

class Segment:
    """
    Класс для получения:
        1) длины отрезка, с округлением до 2 знаков
        2) выявление пересечения отрезка с осью абцисс
        3) выявление пересечения отрезка с осью ординат
    ---------
    Атрибуты:
        point1: Кортеж(tuple) - Первые координаты точек
        point2: Кортеж(tuple) - Вторые координаты точек
    ---------
    Методы:
        length():
            Получает длину отрезка, с округлением до 2 знаков после запятой
        x_axis_intersection():
            Узнает: отрезок пересекает ось абцисс, True = да, False = нет
        y_axis_intersection():
            Узнает: отрезок пересекает ось ординат, True = да, False = нет
    """
    def __init__(self, point1, point2):
        """
        Инициализация необходимых атрибутов для объекта Segment
        :param point1: Кортеж - Первые координаты точек
        :param point2: Кортеж - Вторые координаты точек
        """
        self.point1 = point1
        self.point2 = point2

    def length(self):
        """
        Получить длину отрезка, с округлением до 2 знаков после запятой
        :return: (round(distance, 2)) Длина отрезка, с округлением до 2 знаков
        """
        x1, y1 = self.point1
        x2, y2 = self.point2
        distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        return round(distance, 2)

    def x_axis_intersection(self):
        """
        Узнать отрезок пересекает ось абцисс, True = да, False = нет
        :return: (y1 * y2 <= 0) Сравнение абцисс
        """
        y1 = self.point1[1]
        y2 = self.point2[1]
        return y1 * y2 <= 0

    def y_axis_intersection(self):
        """
        Узнать отрезок пересекает ось ординат, True = да, False = нет
        :return: (x1 * x2 <= 0) Сравнение ординат
        """
        x1 = self.point1[0]
        x2 = self.point2[0]
        return x1 * x2 <= 0

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
