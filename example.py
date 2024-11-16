print('Какой хороший день, предлагаю научиться работать с исключениями')
i = int(input('Введите делитель: '))

try:
    result = 10 * (1 / i)
except ZeroDivisionError as exc:
    print('Нельзя делить на ноль!', exc)
else:
    print('Упа, мы не делим на ноль.')
finally:
    print('finally мы заканчиваем урок')
