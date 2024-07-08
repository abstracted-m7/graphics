import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
# from triangle.plot import plot

# Function to draw a triangle
def draw_triangle(ax):
    # A polygon is a closed two-dimensional figure composed of straight-line segments that meet at their endpoints.
    triangle = Polygon([[0, 0],
                        [1, 0],
                        [0.5, 0.866]],
                        fill=None,
                       edgecolor='black')

    ax.add_patch(triangle)

# Function to translate the triangle
def translate_triangle(ax, dx, dy):
    vertices = [[0, 0],
                [1, 0],
                [0.5, 0.866]]

    translated_vertices = [[v[0] + dx, v[1] + dy] for v in vertices]

    translated_triangle = Polygon(translated_vertices,  fill=None, edgecolor='red')
    ax.add_patch(translated_triangle)

# Main function
def main():
    fig, ax = plt.subplots()

    # Draw the original triangle
    draw_triangle(ax)

    # Translate the triangle
    translate_triangle(ax, 0.5, 0.5)

    # Set plot limits
    ax.set_xlim(-0.5, 2)
    ax.set_ylim(-0.5, 2)

    plt.axis('equal')  # Ensure aspect ratio is maintained
    plt.show()

if __name__ == "__main__":
    main()
