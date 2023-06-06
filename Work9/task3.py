# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
with open('test_file/task_3.txt', 'r') as file:
    purchases = file.read().strip().split('\n\n')
purchases = [[int(price) for price in purchase.split()] for purchase in purchases]
pur_sums = [sum(purchase) for purchase in purchases]
three_most_expensive_purchases = sorted(pur_sums, reverse=True)[:3]
three_most_expensive_purchases = sum(three_most_expensive_purchases)
print('Cумма трёх самых дорогих покупок =', three_most_expensive_purchases)
assert three_most_expensive_purchases == 202346
