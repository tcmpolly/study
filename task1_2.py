# Получаем ввод от пользователя
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
        
print("\nРезультаты операций:")
        
# Сложение
sum_result = num1 + num2
print(f"{num1} + {num2} = {sum_result}")
        
# Вычитание
diff_result = num1 - num2
print(f"{num1} - {num2} = {diff_result}")
        
# Умножение
mul_result = num1 * num2
print(f"{num1} * {num2} = {mul_result}")
        
# Деление с проверкой деления на ноль
if num2 != 0:
    div_result = num1 / num2
else:
    print(f"{num1} / {num2} = Ошибка: деление на ноль!")    
