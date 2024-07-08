import matplotlib.pyplot as plt

def circle_bresenham(xc, yc, r):
    points = []
    x, y = 0, r
    d = 3 - 2 * r

    i=0
    while x <= y:

        points.extend([(xc + x, yc + y), (xc - x, yc + y),
                       (xc + x, yc - y), (xc - x, yc - y),
                        (xc + y, yc + x), (xc - y, yc + x),
                       (xc + y, yc - x), (xc - y, yc - x)])

        print("X: ",x, "\tY: ", y)

        if d < 0:
            x += 1
            y=y
            d += 4 * x + 6 # for east point
        else:
            x += 1
            y -= 1
            d += 4 * (x - y) + 10 # for northeast point

        i += 1


    return points



xc, yc, r = 10,8,8
points = circle_bresenham(xc, yc, r)


xcrd = [p[0] for p in points]
ycrd = [p[1] for p in points]


plt.scatter(xcrd, ycrd, s=20)
plt.axis('equal')  # Ensure aspect ratio is maintained
plt.title("Bresenham's Circle")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()