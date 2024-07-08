
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle

def translate_rectangle(P, T):
    # Create a figure and a set of subplots
    fig, ax = plt.subplots()

    # Original rectangle
    # Rectangle((xmin, ymin), width, height)
    original_rectangle = Rectangle((P[0][0], P[0][1]), P[1][0] - P[0][0], P[1][1] - P[0][1], fill=None, edgecolor='r')
    ax.add_patch(original_rectangle)

    # Calculating translated coordinates

    P[0][0] += T[0]
    P[0][1] += T[1]
    P[1][0] += T[0]
    P[1][1] += T[1]

    # Translated rectangle
    translated_rectangle = Rectangle((P[0][0], P[0][1]), P[1][0] - P[0][0], P[1][1] - P[0][1], fill=None, edgecolor='b')
    ax.add_patch(translated_rectangle)

    # Set limits for x and y axis
    ax.set_xlim([0, 20])
    ax.set_ylim([0, 20])

    plt.show()

if __name__ == "__main__":
    # set cordinates
    P = [[5, 8], [12, 18]]
    # Translation factor
    T = [2, 1]
    translate_rectangle(P, T)
