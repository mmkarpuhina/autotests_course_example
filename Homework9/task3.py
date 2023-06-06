# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
from pathlib import Path
with open(Path.cwd().joinpath('test_file', 'task3.txt'), 'r', encoding='utf-8') as f:
    prices = []
    max_prices = []
    for i in f:
        if i.strip():
            prices.append(int(i.strip()))
        else:
            if prices:
                max_prices.append(sum(prices))
                prices = []
three_most_expensive_purchases = sum(sorted(max_prices)[-3:])

assert three_most_expensive_purchases == 202346
print('Все ок')
