# Напишите функцию multiplication_chain, которая принимает положительное число num,
# и возвращает количество раз count_multy, которое вы должны перемножить цифры числа num и полученных произведений,
# пока не получите одну цифру.
# Например (Ввод --> Вывод) :
#
# 39 --> 3 (потому что 3*9 = 27, 2*7 = 14, 1*4 = 4, вот 4 одна цифра. Итого 3 итерации)
# 999 --> 4 (потому что 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, наконец 1*2 = 2, Итого 4 итерации)
# 4 --> 0 (4 уже одна цифра, а значит мы проделали 0 итераций)

def multiplication_chain(num):
    """
    Получить количество итераций перемноженных цифр числа до одной цифры
    :param num: Число
    :return: (count_multy) Количество итераций
    """
    count_multy = 0
    while len(str(num)) != 1:
        count_multy += 1
        result_multi = 1
        for multi in list(map(int, str(num))):
            result_multi *= multi
        num = result_multi
        print(type(result_multi))
    return count_multy

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    39, 4, 25, 999, 5050, 222333444
]

test_data = [
    3, 0, 2, 4, 1, 4
]


for i, d in enumerate(data):
    assert multiplication_chain(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')