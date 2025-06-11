# Day 2: 30 Days of python programming

# Declaración de variables
first_name = "Alan"
last_name = "García"
full_name = first_name + "Alan Gracía " + last_name
country = "México"
city = "Aguascalientes"
age = 21
year = 2025
is_married = False
is_true = True
is_light_on = True

# Declaración de múltiples variables en una línea
name, hometown, birth_year, is_student = "Alan", "Aguascalientes", 2004, True

# Comprobar los tipos de datos de las variables
print(type(first_name))  # str
print(type(last_name))   # str
print(type(full_name))   # str
print(type(country))     # str
print(type(city))        # str
print(type(age))         # int
print(type(year))        # int
print(type(is_married))  # bool
print(type(is_true))     # bool
print(type(is_light_on)) # bool

# Usando la función len() para encontrar la longitud del nombre
first_name_length = len(first_name)
print(f"Longitud del primer nombre: {first_name_length}")

# Comparar la longitud del primer nombre y el apellido
last_name_length = len(last_name)
print(f"Longitud del apellido: {last_name_length}")
print(f"Diferencia: {abs(first_name_length - last_name_length)}")

# Operaciones aritméticas
num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

print(f"Total: {total}, Diferencia: {diff}, Producto: {product}")
print(f"División: {division:.2f}, Residuo: {remainder}")
print(f"Exponenciación: {exp}, División de piso: {floor_division}")

# Cálculos del círculo
radius = 30
area_of_circle = 3.1416 * radius ** 2
circum_of_circle = 2 * 3.1416 * radius

print(f"Área del círculo: {area_of_circle:.2f}, Circunferencia: {circum_of_circle:.2f}")

# Tomar el radio como entrada del usuario y calcular el área
user_radius = float(input("Ingrese el radio: "))
user_area_of_circle = 3.1416 * user_radius ** 2
print(f"Área del círculo definida por el usuario: {user_area_of_circle:.2f}")

# Usar la función input para obtener información del usuario
first_name = input("Ingrese su primer nombre: ")
last_name = input("Ingrese su apellido: ")
country = input("Ingrese su país: ")
age = int(input("Ingrese su edad: "))

print(f"Hola {first_name} {last_name}, de {country}, con {age} años!")

# Comprobar las palabras clave reservadas en Python
help('keywords')