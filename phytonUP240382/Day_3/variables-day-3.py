# Day 3: 30 Days of python programming

import math

# Declaración de variables
age = 21  # Entero
height = 1.83  # Flotante
complex_number = 3 + 4j  # Número complejo

# Calcular el área de un triángulo
base = float(input("Ingrese la base del triángulo: "))
height = float(input("Ingrese la altura del triángulo: "))
triangle_area = 0.5 * base * height
print(f"El área del triángulo es: {triangle_area}")

# Calcular el perímetro de un triángulo
a = float(input("Ingrese el lado a: "))
b = float(input("Ingrese el lado b: "))
c = float(input("Ingrese el lado c: "))
triangle_perimeter = a + b + c
print(f"El perímetro del triángulo es: {triangle_perimeter}")

# Calcular área y perímetro de un rectángulo
length = float(input("Ingrese la longitud del rectángulo: "))
width = float(input("Ingrese el ancho del rectángulo: "))
rectangle_area = length * width
rectangle_perimeter = 2 * (length + width)
print(f"Área del rectángulo: {rectangle_area}, Perímetro: {rectangle_perimeter}")

# Calcular área y circunferencia de un círculo
radius = float(input("Ingrese el radio del círculo: "))
circle_area = math.pi * radius ** 2
circle_circumference = 2 * math.pi * radius
print(f"Área del círculo: {circle_area:.2f}, Circunferencia: {circle_circumference:.2f}")

# Calcular pendiente, intercepto en x y y de y = 2x - 2
m = 2  # Pendiente
x_intercept = 2 / m  # Cuando y = 0
y_intercept = -2  # Cuando x = 0
print(f"Pendiente: {m}, Intercepto en x: {x_intercept}, Intercepto en y: {y_intercept}")

# Pendiente y distancia euclidiana entre (2,2) y (6,10)
x1, y1, x2, y2 = 2, 2, 6, 10
slope_2 = (y2 - y1) / (x2 - x1)
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"Pendiente: {slope_2}, Distancia euclidiana: {distance:.2f}")

# Comparación de pendientes
print(f"Las pendientes {m} y {slope_2} son {'iguales' if m == slope_2 else 'diferentes'}")

# Evaluar valores de y
x_values = [-3, -2, -1, 0, 1, 2, 3]
for x in x_values:
    y = x**2 + 6*x + 9
    print(f"Para x = {x}, y = {y}")

# Comparaciones y operadores
print(len("python") < len("dragon"))  # Comparación falsa
print("on" in "python" and "on" in "dragon")  # Comprobación con operador and
print("jargon" in "I hope this course is not full of jargon.")  # Verificación con operador in
print("on" not in "python" and "on" not in "dragon")  # Comprobación de ausencia

# Conversión de tipos de datos
python_length = len("python")
print(float(python_length))
print(str(python_length))

# Comprobar si un número es par
num = int(input("Ingrese un número para verificar si es par: "))
print(f"{num} es {'par' if num % 2 == 0 else 'impar'}")

# Comparaciones de tipos y valores
print(7 // 3 == int(2.7))
print(type("10") == type(10))
print(int(float("9.8")) == 10)

# Calcular el pago según horas trabajadas
hours = float(input("Ingrese horas trabajadas: "))
rate = float(input("Ingrese tarifa por hora: "))
pay = hours * rate
print(f"Su pago semanal es: {pay}")

# Calcular los segundos vividos en base a años
years_lived = float(input("Ingrese los años que ha vivido: "))
seconds_lived = years_lived * 365 * 24 * 60 * 60
print(f"Has vivido aproximadamente {seconds_lived} segundos.")

# Generar la tabla de números
for i in range(1, 6):
    print(f"{i} {1} {i} {i**2} {i**3}")