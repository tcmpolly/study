# Получаем номер месяца от пользователя
month = int(input("Введите номер месяца (от 1 до 12): "))

# Определяем время года
if 1 <= month <= 2 or month == 12:
    season = "зима"
elif 3 <= month <= 5:
    season = "весна"
elif 6 <= month <= 8:
    season = "лето"
elif 9 <= month <= 11:
    season = "осень"
else:
    season = "некорректный месяц"

# Выводим результат
print(f"Месяц {month} — это {season}.")