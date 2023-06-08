# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

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


@pytest.mark.parametrize(
    "value, result",
    [
        pytest.param((20, 2, 0), None, marks=pytest.mark.xfail),
        pytest.param((10, 2), 5, marks=pytest.mark.smoke),
        ((100, 5, 2), 10),
        pytest.param((8, 4, 2), 1, marks=pytest.mark.skip),
        ((-10, 2, 5), -1)
    ]
)
def test_all_division(value, result):
    """
    Проверка функции all_division для различных входных параметров.
    :param value: Кортеж, содержащий значения для a, b и c
    :param result: Результат вычисления:
     1) результат равен None - исключения ZeroDivisionError
     2) результат положительный/отрицательный

    --------
    Параметры:
    (20, 2, 0) - ожидается исключение ZeroDivisionError.
    (10, 2) - smoke.
    (100, 5, 2) - ожидается результат 10.
    (8, 4, 2) - skip.
    (-10, 2, 5) - ожидается результат -1.
    """
    if result is None:
        with pytest.raises(ZeroDivisionError):
            all_division(*value)
    else:
        assert all_division(*value) == result
