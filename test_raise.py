def greet_person(person_name):
    if person_name == 'ВоланДеМорт':
        raise Exception('Мы не любим тебя, ВоланДеМорт')
    print(f'Привет {person_name}')


greet_person('Дорогой ученик')
# greet_person('ВоланДеМорт')

print()

try:
    raise NameError('Привет Там')
except NameError as exc:
    print(f'Исключение типа {type(exc)} пролетело мимо! его параметры {exc.args}')
    # raise

print()


class ProZero(Exception):
    def __init__(self, message, extra_info):
        self.message = message
        self.extra_info = extra_info


def f(a, b):
    if b == 0:
        raise ProZero('Деление на ноль не возможно', {'a': a, 'b': b})
    return a / b


try:
    result = f(10, 0)
    print(result)
except ProZero as exc:
    print('Не очень хороший день, мы словили ошибку.')
    print(f'Сообщение об ошибке: {exc.message}')
    print(f'Дополнительная информация: {exc.extra_info}')
