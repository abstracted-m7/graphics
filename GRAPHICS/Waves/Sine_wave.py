# Algo :
# Step 1: START
# Step 2: Importing the libraries as numpy and mathplotlib.
# Step 3: Declear the line sequance and sinx.
# Step 4: Draw the line of the graph.
# Step 5: Declear the labels of the graph.
# Step 6: Denoted sets the x & y axis limits for the current axes or chart.
# Step 7: Print
# Step 8: STOP
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,4*np.pi,100)# x gose 0 to 100
sinx=np.sin(x)#function denoted the sinx
plt.plot(x,sinx)#using plot create the sine wave(line)
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Sine wave")
plt.xlim(0,4*np.pi)# x-axis line range
plt.ylim(-1.5,1.5)#y-axis line range
plt.show()#show the result