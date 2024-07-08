# Algo :
# Step 1: START
# Step 2: Importing the libraries as numpy and mathplotlib.
# Step 3: Declear the line sequance.
# Step 4: Draw the line of the graph.
# Step 5: Declear the labels of the graph.
# Step 6: Denoted sets the x & y axis limits for the current axes or chart.
# Step 7: Print
# Step 8: STOP
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(2,2*np.pi,500)
plt.plot(x,label="x")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Straight line")
plt.xlim(0,2*np.pi)
plt.ylim(0,4)
plt.legend()
plt.show()