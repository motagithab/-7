number1 = int(input('Введите первое число: '))
number2 = int(input('Введите второе число: '))
number3 = int(input('Введите третье число: '))
if number1 > number2 and number1 > number3:
    print('Максимальное число: ', str(number1))
elif number2 > number3 and number2 > number1:
    print('Максимальное число: ', str(number2))
elif number3 > number1 and number3 > number2:
    print('Максимальное число: ', str(number3))