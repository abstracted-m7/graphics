import matplotlib.pyplot as plt

# Function to scale coordinates
def scale_coordinates(coordinates, Sx, Sy):
    scaled_coordinates = [(x * Sx, y * Sy) for x, y in coordinates]
    return scaled_coordinates

# Scale factor (e.g., 2 means scaling to double size)
Sx = 1.5
Sy = 0.5

# Define the original coordinates of the object
original_coordinates = [(4,4),(5,2.5),(3,2.5),(4,4)]

xcrd_original = [m[0] for m in original_coordinates]
ycrd_original = [m[1] for m in original_coordinates]

# Plot original object
plt.plot(xcrd_original, ycrd_original, label='Original')

# Get scaled coordinates
scaled_coordinates = scale_coordinates(original_coordinates, Sx, Sy)

xcrd_scale = [p[0] for p in scaled_coordinates]
ycrd_scale = [p[1] for p in scaled_coordinates]

# Print the coordinates
points = [xcrd_scale, ycrd_scale]
print(points)

# Plot scaled object
plt.plot(xcrd_scale, ycrd_scale, label='Scaled')

# Set equal aspect ratio to maintain proportions
plt.axis('equal')

# Set labels and legend
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()

# Show plot
plt.grid()
plt.show()
