user_input = input("Введите строку: ").lower().replace(" ", "")
if user_input == user_input[::-1]:
    print("Да, это палиндром")
else:
    print("Нет, это не палиндром")