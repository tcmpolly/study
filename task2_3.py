# Получаем тип конвертации от пользователя
print("Выберите тип конвертации:")
print("1 - Цельсий → Фаренгейт")
print("2 - Фаренгейт → Цельсий")
choice = int(input("Ваш выбор (1 или 2): "))

# Выполняем конвертацию в зависимости от выбора
if choice == 1:
    # Конвертируем из Цельсия в Фаренгейт
    celsius = float(input("Введите температуру в градусах Цельсия: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C = {fahrenheit:.1f}°F")
    
elif choice == 2:
    # Конвертируем из Фаренгейта в Цельсий
    fahrenheit = float(input("Введите температуру в градусах Фаренгейта: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F = {celsius:.1f}°C")
    
else:
    print("Ошибка! Выберите 1 или 2.")