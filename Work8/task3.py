# Напишите функцию segment
# На вход подается два кортежа с координатами точек (x1, y1), (x2, y2)

# В функции происходит проверка на корректность полученных данных.
# С помощью инструкции try/except as отлавливается исключение Exception. И если это исключение поймано,
# то функция возвращает текст исключения задом наперед (Нужно обратится к атрибуту экземпляра класса Exception)
# Если исключения не произошло, то функция возвращает сумму всех координат


def segment(point1, point2):
    """
    Получить сумму всех координат, если нет ошибки, иначе вернуть текст исключения задом наперед
    :param point1: Первые координаты
    :param point2: Вторые координаты
    :return: (''.join(reversed(str(typeerror.args[0])))) Текст исключения задом наперед
    """
    try:
        sum_tuple = point1[0] + point1[1] + point2[0] + point2[1]
        return sum_tuple
    except Exception as error:
        return ''.join(reversed(str(error.args[0])))


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    ((2, 3), (4, 5)),
    ((2, -3), (4, 5)),
    ((2, 3), ('4', 5)),
    (('a', 3), (4, 5)),
]

test_data = [
    14,
    8,
    "'rts' dna 'tni' :+ rof )s(epyt dnarepo detroppusnu",
    'rts ot )"tni" ton( rts etanetacnoc ylno nac']


for i, d in enumerate(data):
    assert segment(*d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
