try:
    i = int(input('Введите делитель: '))
    print(10 / i)
    print('Сделано')
except:
    print('Нельзя делить на ноль!')

try:
    i = 0
    print(10 / i)
    print('Сделано')
except ZeroDivisionError:  # указываем конкретный класс ошибки
    print('Нельзя делить на ноль!')

try:
    truba = a + b
    truba = 10 / 0
except (ZeroDivisionError, NameError):  # указываем имена классов ошибок
    print('Что-то пошло не так.')

try:
    truba = a + b
    truba = 10 / 0
except ZeroDivisionError:  # указываем имена классов ошибок
    print('Что-то пошло не так.')
except NameError:  # указываем имена классов ошибок
    print('Что-то пошло как-то так.')

try:
    a = 10 / 0
except ZeroDivisionError as exc:  # указываем конкретный класс ошибки
    print(f'Вот что пошло не так - {exc}, но мы ещё на плаву.')

try:
    file = open('blabla.txt')
except OSError as exc:  # указываем конкретный класс ошибки
    print(f'Вот что пошло не так - {exc} параметры {exc.args}, но мы ещё на плаву.')