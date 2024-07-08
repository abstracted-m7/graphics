import matplotlib.pyplot as plt

def dda_algo(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0


    # if abs(dx) >= abs(dy): # check condition
    #     steps = abs(dx) #Find track of x
    # else:
    #     steps = abs(dy) #Find track of y

    steps = abs(max(dx, dy))

    # delx = dx / steps
    # dely = dy / steps

    x = x0
    y = y0

    xcd = [x0]
    ycd = [y0]

    p = 2 * dy - dx

    for i in range(0, steps):
        if p < 0:
            x += 1
            p += 2 * dy

        else:
            x += 1
            y += 1
            p += ((2*dy) - (2*dx))

        print("X0: ", format(x, ".1f"), "Y0", y)
        xcd.append(x)
        ycd.append(y)

    plt.plot(xcd, ycd)
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    plt.title("Bresenham's Algorithm\n|m| < 1")
    plt.show()

if __name__ == "__main__":
    x0, y0 = 0,2
    x1, y1 = 4,5
    dda_algo(x0, y0, x1, y1)