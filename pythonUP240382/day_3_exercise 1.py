# Day 2: Practice All-in-One

# 1. Age (integer), height (float), complex number
age = 30
height = 1.75
complex_num = 2 + 3j

# 2. Area of a triangle
base = float(input("Enter base: "))
height_input = float(input("Enter height: "))
area_triangle = 0.5 * base * height_input
print("The area of the triangle is", area_triangle)

# 3. Perimeter of a triangle
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
perimeter_triangle = a + b + c
print("The perimeter of the triangle is", perimeter_triangle)

# 4. Rectangle area and perimeter
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area_rectangle = length * width
perimeter_rectangle = 2 * (length + width)
print("Area:", area_rectangle, "| Perimeter:", perimeter_rectangle)

# 5. Circle calculations from radius
radius = float(input("Enter radius: "))
pi = 3.14
area_circle = pi * radius ** 2
circumference = 2 * pi * radius
print("Area of circle:", area_circle)
print("Circumference:", circumference)

# 6. Slope, x-intercept, y-intercept of y = 2x - 2
slope = 2
x_intercept = 2 / 2  # when y=0 => 0 = 2x -2
y_intercept = -2     # when x=0
print("Slope:", slope)
print("x-intercept:", x_intercept)
print("y-intercept:", y_intercept)

# 7. Slope and Euclidean distance between two points
x1, y1 = 2, 2
x2, y2 = 6, 10
slope_2 = (y2 - y1) / (x2 - x1)
import math
euclidean_distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Slope:", slope_2)
print("Euclidean distance:", euclidean_distance)

# 8. Compare slopes
print("Are slopes equal?", slope == slope_2)

# 9. Solve y = x² + 6x + 9
for x in range(-10, 1):
    y = x ** 2 + 6 * x + 9
    print(f"x = {x}, y = {y}")

# 10. Length comparison
print("Is len('python') != len('dragon')?", len("python") != len("dragon"))

# 11. 'on' in both?
print("'on' in both?", "on" in "python" and "on" in "dragon")

# 12. 'jargon' in sentence?
sentence = "I hope this course is not full of jargon."
print("'jargon' in sentence?", "jargon" in sentence)

# 13. Not in both
print("There is no 'on' in both python and dragon?", "on" not in "python" and "on" not in "dragon")

# 14. Length conversions
length_python = len("python")
print("Float:", float(length_python))
print("String:", str(length_python))

# 15. Check if even
num = int(input("Enter a number: "))
print("Even?" , num % 2 == 0)

# 16. Floor division vs int(2.7)
print("7 // 3 == int(2.7)?", 7 // 3 == int(2.7))

# 17. Type comparison
print("Same type?", type('10') == type(10))

# 18. Convert '9.8' to int and compare
try:
    result = int('9.8') == 10
except ValueError:
    result = False
print("int('9.8') == 10?", result)

# 19. Weekly pay
hours = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))
earnings = hours * rate
print("Your weekly earning is", earnings)

# 20. Life seconds
years_lived = int(input("Enter number of years you have lived: "))
seconds = years_lived * 365 * 24 * 60 * 60
print("You have lived for", seconds, "seconds.")

# 21. Display table
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")