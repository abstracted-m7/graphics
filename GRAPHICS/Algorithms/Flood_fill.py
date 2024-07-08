import numpy as np
import matplotlib.pyplot as plt

def flood_fill(image, x, y, new_color):
    original_color = image[x, y]
    if original_color == new_color:
        return

    def fill(x, y):
        if (x < 0 or x >= image.shape[0] or
            y < 0 or y >= image.shape[1] or
            image[x, y] != original_color):
            return

        image[x, y] = new_color

        fill(x + 1, y)
        fill(x - 1, y)
        fill(x, y + 1)
        fill(x, y - 1)

    fill(x, y)

# Create an example image (a 2D numpy array)
image = np.array([[1, 1, 1, 2, 2, 2],
                  [1, 1, 1, 2, 2, 2],
                  [1, 1, 1, 2, 2, 2],
                  [3, 3, 3, 4, 4, 4],
                  [3, 3, 3, 4, 4, 4],
                  [3, 3, 3, 4, 4, 4]])

# Print the original image
print("Original Image:")
print(image)

# Plot the original image
plt.imshow(image, cmap='gray', interpolation='none')
plt.title('Original Image')
plt.show()

# Perform flood fill on the image
flood_fill(image, 1, 1, 9)

# Print the filled image
print("Filled Image:")
print(image)

# Plot the filled image
plt.imshow(image, cmap='gray', interpolation='none')
plt.title('Filled Image')
plt.show()
