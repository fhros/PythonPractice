
import numpy as np

def radians_to_degrees(radians):
    return np.round(radians * (180 / np.pi), 2)

def degrees_to_radians(degrees):
    return np.round(degrees * (np.pi / 180), 2)

def angle_table():
    degrees = np.array([30, 45, 60, 90, 120, 135, 150, 180, 270, 360])
    radians = degrees_to_radians(degrees)
    return np.column_stack((degrees, radians))

# tehtävä 1
print("tehtävä 1:")
print("a)", radians_to_degrees(2.493))
print("b)", radians_to_degrees(0.911))

# tehtävä 2
print("tehtävä 2:")
print("a)", degrees_to_radians(137.7))
print("b)", degrees_to_radians(62.3))

# tehtävä 3
print("tehtävä 3:")
print(angle_table())