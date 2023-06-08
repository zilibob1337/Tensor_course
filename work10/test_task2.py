# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):
    """
    Получить кортеж данных и последовательное деление каждого числа в кортеже.
    :param arg1: Кортеж данных
    :return: Результат деления
    """
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


def test_1():
    """
    Проверка исключения ZeroDivisionError при делении на ноль
    :return: ZeroDivisionError
    """
    with pytest.raises(ZeroDivisionError):
        all_division(20, 2, 0)


def test_2():
    """
    Проверка деления данных (10, 2). ОР: 5
    :return: 5
    """
    assert all_division(10, 2) == 5


def test_3():
    """
    Проверка деления данных (100, 5, 2). ОР: 10
    :return: 10
    """
    assert all_division(100, 5, 2) == 10


def test_4():
    """
    Проверка деления данных (8, 4, 2). ОР: 1
    :return: 1
    """
    assert all_division(8, 4, 2) == 1


def test_5():
    """
    Проверка деления данных (-10, 2, 5). ОР: -1
    :return: -1
    """
    assert all_division(-10, 2, 5) == -1


@pytest.mark.smoke
def test_all_division_smoke():
    """
    SMOKE-тест. Проверка деления данных (10, 2). ОР: 5.
    :return: 5
    """
    assert all_division(10, 2) == 5


def test_mask1():
    """
    Тест по МАСКЕ. Проверка деления данных (8, 4, 2). ОР: 1.
    :return: 1
    """
    assert all_division(8, 4, 2) == 1


def test_mask2():
    """
    Тест по МАСКЕ. Проверка деления данных (-10, 2, 5). ОР: -1.
    :return: -1
    """
    assert all_division(-10, 2, 5) == -1
