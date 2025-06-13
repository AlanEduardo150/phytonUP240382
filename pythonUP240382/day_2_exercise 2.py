# Day 2: Python Variables and Built-in Functions

# Variable declarations
first_name = "Alan"
last_name = "García"
full_name = first_name + "Alan García " + last_name
country = "Mexico"
city = "Aguascalientes"
age = 21
year = 2004
is_married = False
is_true = True
is_light_on = True
a, b, c = 1, 2.5, "Python"

# Check the data type using type()
print(type(first_name))     # str
print(type(age))            # int
print(type(is_married))     # bool
print(type(a), type(b), type(c))  # int float str

# Length of first name
print("Length of first name:", len(first_name))

# Compare first name and last name length
print("First name longer than last name?", len(first_name) > len(last_name))

# Arithmetic operations
num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

print("Total:", total)
print("Difference:", diff)
print("Product:", product)
print("Division:", division)
print("Remainder:", remainder)
print("Exponent:", exp)
print("Floor Division:", floor_division)

# Circle calculations
radius = 30
pi = 3.14159

area_of_circle = pi * radius ** 2
circum_of_circle = 2 * pi * radius

print("Area of circle:", area_of_circle)
print("Circumference of circle:", circum_of_circle)

# User input for radius
user_radius = float(input("Enter the radius of a circle: "))
user_area = pi * user_radius ** 2
print("Area from user input:", user_area)

# User info input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = input("Enter your age: ")

print(f"Hi {first_name} {last_name} from {country}, age {age}!")

# Check Python reserved keywords
help('keywords')