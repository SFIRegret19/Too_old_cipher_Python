def password(n):
    combination_list = ''
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if i == j:
                continue
            elif (n % (i + j) == 0) or (i + j == n):
                combination_list += (str(i) + str(j))
    return combination_list

n = int(input("Введите число от 3 до 20: "))

if n >= 3 and n <= 20:
    print(password(n))
else:
    print('Введите число от 3 до 20')