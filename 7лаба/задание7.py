def подсчет_букв():
    гласные = "аеёиоуыэюя"
    согласные = "бвгджзйклмнпрстфхцчшщ"
    строка = input("Введите строку: ")
    кол_гласных = sum(1 for буква in строка if буква.lower() in гласные)
    кол_согласных = sum(1 for буква in строка if буква.lower() in согласные)
    print(f"Количество гласных: {кол_гласных}")
    print(f"Количество согласных: {кол_согласных}")

подсчет_букв()