import pytest
import time


@pytest.fixture(scope='class')
def timer(request):
    """
    Фикстура для замера времени выполнения всех тестов.
    :param request: объект с информацией о тесте
    :return: время выполнения всех тестов
    """
    start_time = time.time()
    yield
    end_time = time.time()
    print('Время выполнения ВСЕХ тестов: {}'.format(end_time - start_time))


@pytest.fixture
def test_timer():
    """
    Фикстура для замера времени выполнения отдельного теста.
    :return: время выполнения одного теста
    """
    start_time = time.time()
    yield
    end_time = time.time()
    print('\nВремя выполнения теста: {}'.format(end_time - start_time))
