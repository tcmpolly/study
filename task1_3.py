# Запрашиваем четырёхзначное число
print("Введите четырёхзначное число (например, 1234):")
number_str = input().strip()

# Проверяем, что введено ровно 4 символа
if len(number_str) != 4:
    print("Ошибка: нужно ввести ровно 4 цифры!")
else:
    # Делим строку на две части
    ab = number_str[:2]  # первые 2 символа
    cd = number_str[2:]  # последние 2 символа

    # Преобразуем в числа и складываем
    ab_int = int(ab)
    cd_int = int(cd)
    total = ab_int + cd_int

    print(f"Сумма ab + cd = {ab_int} + {cd_int} = {total}")