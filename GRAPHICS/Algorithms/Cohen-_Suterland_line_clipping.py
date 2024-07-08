
import matplotlib.pyplot as plt

# Define constants for region codes
INSIDE = 0  # 0000
LEFT = 1    # 0001
RIGHT = 2   # 0010
BOTTOM = 4  # 0100
TOP = 8     # 1000

# Function to compute the region code for a point (x, y)
def compute_code(x, y, x_min, y_min, x_max, y_max):
    code = INSIDE
    if x < x_min:
        code |= LEFT  #bitwise OR operation " |= "
    elif x > x_max:
        code |= RIGHT
    if y < y_min:
        code |= BOTTOM
    elif y > y_max:
        code |= TOP
    return code

# Cohen-Sutherland clipping algorithm
def cohen_sutherland_clip(x1, y1, x2, y2, x_min, y_min, x_max, y_max):
    code1 = compute_code(x1, y1, x_min, y_min, x_max, y_max)
    code2 = compute_code(x2, y2, x_min, y_min, x_max, y_max)
    accept = False

    while True:
        if code1 == 0 and code2 == 0:
            accept = True
            break
        elif code1 & code2 != 0:
            break
        else:
            code_out = code1 if code1 != 0 else code2
            if code_out & TOP:
                x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
                y = y_max
            elif code_out & BOTTOM:
                x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
                y = y_min
            elif code_out & RIGHT:
                y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
                x = x_max
            elif code_out & LEFT:
                y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
                x = x_min

            if code_out == code1:
                x1, y1 = x, y
                code1 = compute_code(x1, y1, x_min, y_min, x_max, y_max)
            else:
                x2, y2 = x, y
                code2 = compute_code(x2, y2, x_min, y_min, x_max, y_max)

    if accept:
        return (x1, y1, x2, y2)
    else:
        return None

# Example usage
x_min, y_min, x_max, y_max = 10, 10, 200, 200
x1, y1 = 5, 5
x2, y2 = 150, 150

clipped_line = cohen_sutherland_clip(x1, y1, x2, y2, x_min, y_min, x_max, y_max)

if clipped_line:
    print("Clipped line coordinates:", clipped_line)
else:
    print("Line is outside the clipping window.")

# Plotting the lines
plt.figure()
plt.plot([x1, x2], [y1, y2], 'r--', label="Original Line")
if clipped_line:
    plt.plot([clipped_line[0], clipped_line[2]], [clipped_line[1], clipped_line[3]], 'b-', label="Clipped Line")

# Plot the clipping window
plt.plot([x_min, x_max], [y_min, y_min], 'k-')
plt.plot([x_min, x_max], [y_max, y_max], 'k-')
plt.plot([x_min, x_min], [y_min, y_max], 'k-')
plt.plot([x_max, x_max], [y_min, y_max], 'k-')

plt.xlim(0, 210)
plt.ylim(0, 210)
plt.title("Cohen-Sutherland Clipping Algorithm")
plt.legend()
plt.show()
