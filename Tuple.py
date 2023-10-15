# Creating a tuple
coordinates = (10, 20)
print("Coordinates:", coordinates)

# Accessing tuple elements
x = coordinates[0]
y = coordinates[1]
print("X-coordinate:", x)
print("Y-coordinate:", y)

# Tuples are immutable (cannot be modified)
try:
    coordinates[0] = 50  # Trying to modify the tuple
except TypeError as error:
    print("Error:", error)

# Tuples can be nested
nested_tuple = (coordinates, (30, 40))
print("Nested tuple:", nested_tuple)

# Unpacking tuples
point1, point2 = nested_tuple
print("Point1:", point1)
print("Point2:", point2)

# Tuples can be used as function arguments
def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return distance

distance = calculate_distance(coordinates, (50, 60))
print("Distance:", distance)
