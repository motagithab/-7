def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result

number = int(input("Введите целое неотрицательное число: "))

if number < 0:
    print("Введите целое неотрицательное число.")
else:
    result = factorial(number)
    print(f"Факториал числа {number} равен {result}.")