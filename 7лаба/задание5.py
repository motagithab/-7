numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in numbers:
    for j in numbers:
        print(str(i) + '*' + str(j) + '=' + str(i*j))
    print()