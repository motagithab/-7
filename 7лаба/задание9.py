n = int(input("Введите натуральное число n: "))

if n < 1:
    print("Пожалуйста, введите натуральное число больше 0.")
else:
    for i in reversed(range(1, n+1)):
        print(i)