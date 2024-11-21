def calc(line):
    operand_1, operation, operand_2 = line.split(' ')
    operand_1 = int(operand_1)
    operand_2 = int(operand_2)
    if operation == '+':
        value = operand_1 + operand_2
        print(f'Результат: {value}')
    elif operation == '-':
        value = operand_1 - operand_2
        print(f'Результат: {value}')
    elif operation == '/':
        value = operand_1 / operand_2
        print(f'Результат: {value}')
    elif operation == '*':
        value = operand_1 / operand_2
        print(f'Результат: {value}')
    elif operation == '//':
        value = operand_1 // operand_2
        print(f'Результат: {value}')
    elif operation == '%':
        value = operand_1 % operand_2
        print(f'Результат: {value}')
    else:
        raise ValueError('Unknown operation {operation}')
    return value


total = 0
cnt =0
with open('calc.txt') as file:
    for line in file:
        cnt += 1
        try:
            total += calc(line)
        except ValueError as exc:
            if 'unpack' in exc.args[0]:
                print(f'Ошибка в линии {cnt}, не хватает операндов {exc} в строке {line}')
            else:
                print(f'Ошибка в линии {cnt}, не могу преобразовать к целому {exc} в строке {line}')

print(f'Total {total}')