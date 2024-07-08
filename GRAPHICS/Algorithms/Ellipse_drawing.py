import matplotlib.pyplot as plt

def midpoint_ellipse(rx, ry, xc, yc):
    x = 0
    y = ry
    rx2 = rx ** 2
    ry2 = ry ** 2
    tworx2 = 2 * rx2
    twory2 = 2 * ry2
    px = 0
    py = tworx2 * y

    points = []

    # Region 1
    p1 = ry2 - (rx2 * ry) + (0.25 * rx2)
    while px < py:
        points.append((xc + x, yc + y))
        points.append((xc - x, yc + y))
        points.append((xc + x, yc - y))
        points.append((xc - x, yc - y))

        x += 1
        px += twory2
        if p1 < 0:
            p1 += ry2 + px
        else:
            y -= 1
            py -= tworx2
            p1 += ry2 + px - py

    # Region 2
    p2 = (ry2 * (x + 0.5) ** 2) + (rx2 * (y - 1) ** 2) - (rx2 * ry2)
    while y >= 0:
        points.append((xc + x, yc + y))
        points.append((xc - x, yc + y))
        points.append((xc + x, yc - y))
        points.append((xc - x, yc - y))

        y -= 1
        py -= tworx2
        if p2 > 0:
            p2 += rx2 - py
        else:
            x += 1
            px += twory2
            p2 += rx2 - py + px

    return points

def plot_ellipse(points):
    x_vals = [p[0] for p in points]
    y_vals = [p[1] for p in points]

    plt.plot(x_vals, y_vals, 'ro')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Midpoint Ellipse Drawing Algorithm')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

# Parameters for the ellipse
rx = 8  # Radius along x-axis
ry = 10 # Radius along y-axis
xc = 7 # Center x-coordinate
yc = 7 # Center y-coordinate

# Get the points
ellipse_points = midpoint_ellipse(rx, ry, xc, yc)

# # Print the points
# for point in ellipse_points:
#     print(point)

# Plot the ellipse
plot_ellipse(ellipse_points)
