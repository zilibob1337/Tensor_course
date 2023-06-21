# Есть маркер @pytest.mark.id_check(1, 2, 3), нужно вывести на печать, то что в него передано
#
# >>> 1, 2, 3

import pytest


@pytest.mark.id_check(1, 2, 3)
def test():
    marker = getattr(test, 'pytestmark')[0]  # получаем объект маркера
    id_check = marker.args  # получаем список параметров, переданных в маркер
    print(f'\n{id_check}')
    pass
