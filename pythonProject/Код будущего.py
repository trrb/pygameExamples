def summ(num1: float, num2:float) -> float:
    return num1 + num2

def difference(num1: float, num2: float) -> float:
    return num1 - num2

def composition(num1: float, num2: float) -> float:
    return num1 * num2

def division(num1: float, num2: float) -> float:
    if num2 != 0:
        return num1 / num2
    else:
        return "Ошибка! На нуль делить нельзя!"


print('Простой калькулятор, введите два числа:')
number1 = int(input())
number2 = int(input())
print(f'ваши числа {number1} и {number2}')
print("какое действие хотите с ними использовать?:")
action = input()
if action == '+':
    print(f'{number1} + {number2} = {summ(number1, number2)}')
elif action == '-':
    print(f'{number1} - {number2} = {difference(number1, number2)}')
elif action == '*':
    print(f'{number1} * {number2} = {composition(number1, number2)}')
elif action == '/':
    print(f'{number1} / {number2} = {division(number1, number2)}')
else:
    print('в таком простом калькуляторе нет такого действия ;(')