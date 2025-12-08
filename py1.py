import cmath

# Guide the user for input
print("Enter a, b, and c for the quadratic equation ax² + bx + c = 0")

# Take input for coefficients a, b, and c
a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))

# Calculate the discriminant
discriminant = (b ** 2) - (4 * a * c)

# Calculate the two roots using the quadratic formula
root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)

# Print the roots
print("The roots of the quadratic equation are:")
print("Root 1:", root1)
print("Root 2:", root2)
