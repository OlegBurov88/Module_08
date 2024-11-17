# ошибки летят по стеку вызовов функций
def f1(number):
    return 10 / number


def f2():
    print('Какой хороший день.')
    result_f1 = f1(0)
    return result_f1

# total = f2()
try:
    total = f2()
    print(total)
except ZeroDivisionError as exc:
    print(f'вот что пошло не так - {exc}, но мы устояли')

print()

def f1_1(number):
    return 10 / number


def f2_1():
    print('Какой хороший день.')
    summ = 0
    for i in range(-2, 2):
        summ += f1_1(number=i)
        print(summ)
    return summ

# total = f2_1()
try:
    total = f2_1()
except ZeroDivisionError as exc:
    print(f'вот что пошло не так - {exc}, но мы устояли')

print()

def f1_2(number):
    return 10 / number


def f2_2():
    summ = 0
    for i in range(-2, 3, 1):
        try:
            summ += f1_2(i)
            print(summ)
        except ZeroDivisionError as exc:
            print(f'внутри f1_2 что-то пошло не так: {exc}, но мы устояли')
    return summ / 0


try:
    total = f2_2()
    print(f'Вот ваш результат функции: {total}')
except ZeroDivisionError as exc:
    print(f'внутри f2 что-то пошло не так: {exc}, но мы устояли')

print()

def f1_3(number):
    return total / number


def f2_3():
    summ = 0
    for i in range(2, -1, -1):
        try:
            summ += f1_3(number=i)
            print(summ)
        except ZeroDivisionError as exc:
            print(f'внутри f1 что-то пошло не так: {exc}, но мы устояли')
    return summ / 0


try:
    f2_3()
except ZeroDivisionError as exc:
    print(f'внутри f2 что-то пошло не так: {exc}, но мы устояли')