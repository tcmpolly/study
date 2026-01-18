import math

def rectangle_area():
    """Вычисляет площадь прямоугольника."""
    print("\nПлощадь прямоугольника")
    width = float(input("Введите ширину: "))
    height = float(input("Введите высоту: "))
    area = width * height
    return area

def circle_area():
    """Вычисляет площадь круга."""
    print("\nПлощадь круга")
    radius = float(input("Введите радиус: "))
    area = math.pi * radius ** 2
    return area

def triangle_area():
    """Вычисляет площадь треугольника."""
    print("\nПлощадь треугольника")
    base = float(input("Введите основание: "))
    height = float(input("Введите высоту: "))
    area = 0.5 * base * height
    return area
    

# Основная программа
print("КАЛЬКУЛЯТОР ПЛОЩАДЕЙ ФИГУР")

print("\nВыберите фигуру:")
print("1. Прямоугольник")
print("2. Круг")
print("3. Треугольник")
    
choice = input("Ваш выбор (1-3): ")
    
if choice == "1":
        area = rectangle_area()
        if area is not None:
            print(f"Площадь прямоугольника: {area:.2f}")
elif choice == "2":
        area = circle_area()
        if area is not None:
            print(f"Площадь круга: {area:.2f}")
elif choice == "3":
        area = triangle_area()
        if area is not None:
            print(f"Площадь треугольника: {area:.2f}")
else:
        print("Неверный выбор! Попробуйте снова.")
    