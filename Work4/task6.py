# Напишите функцию, которая принимает кортеж num_tuple из 10 цифр num_tuple,
# и возвращает строку этих чисел в виде номера телефона str_phone.
# Например (Ввод --> Вывод) :
# (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)  => "(123) 456-7890"

def create_phone_number(num_tuple):
    """
    Получить номер телефона в формате "(nnn) nnn-nnnn" из кортежа 10 цифр
    :param num_tuple: Кортеж 10 цифр
    :return: (str_phone) Новый формат телефона
    """
    str_phone = ''
    i_1 = 0
    while i_1 < 3:
        if '(' not in str_phone:
            str_phone += '('
        str_phone = str_phone + str(num_tuple[i_1])
        i_1 += 1
    str_phone += ') '
    while i_1 < 6:
        str_phone = str_phone + str(num_tuple[i_1])
        i_1 += 1
    str_phone += '-'
    while i_1 < 10:
        str_phone = str_phone + str(num_tuple[i_1])
        i_1 += 1
    print(str_phone)
    return str_phone

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    (1, 2, 3, 4, 5, 6, 7, 8, 9, 0),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (0, 2, 3, 0, 5, 6, 0, 8, 9, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
]

test_data = [
    "(123) 456-7890", "(111) 111-1111", "(023) 056-0890", "(000) 000-0000"
]


for i, d in enumerate(data):
    assert create_phone_number(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')