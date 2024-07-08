import matplotlib.pyplot as plt

def dda_algo(x0, y0, x1, y1):

    dx = x1-x0
    dy = y1-y0

    if abs(dx) >= abs(dy): # check condition
        span = abs(dx) #Find track of x
    else:
        span = abs(dy) #Find track of y

    delx = (dx)/span #Find iteration of x
    dely = (dy)/span #Find iteration of y


    # loop increment
    i = 1

    # Empty list for storing coordinets
    xcd = []
    ycd = []

    #Declear the loop with the condition
    while i <= span:
        i += 1
        x0 = x0 + delx
        y0 = y0 + dely
        print("X0: ", format(x0, ".1f"), "Y0", y0)
        xcd.append(x0)
        ycd.append(y0)
    plt.plot(xcd, ycd)
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    plt.title("DDA Algorithm\n|m| <= 1")

    plt.show()

if __name__ == "__main__":
    x0, y0 = 0, 0
    x1, y1 = 6, 6
    dda_algo(x0, y0, x1, y1)