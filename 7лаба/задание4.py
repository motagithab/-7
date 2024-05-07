number = int(input('Введите целое число больше единицы: '))
if number < 1:
    print('ERROR')
elif number == 2:
    print(str(number) + ' простое число')
else:
    is_prime = True
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print(str(number) + ' простое число')
    else:
        print(str(number) + ' не является простым числом')