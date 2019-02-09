import pytest
import matplotlib.pyplot as plt
import numpy as np

# Creating random data for test plot 
N = 500
x = np.random.rand(N)
y = np.random.rand(N)
z = np.random.rand(N)
colors = (0,0,0)
area = np.pi*3
 
# Plotting a scatterplot with parameters to test 
plt.scatter(x, y, c="red", alpha=0.5, label = "y")
plt.scatter(x, z, c="blue", alpha=0.5, label = "z")
plt.legend(loc="upper right",title = "hi")
plt.rcParams['axes.facecolor']= "white"
plt.rcParams['axes.titlesize'] = 20
plt.rcParams['axes.edgecolor'] = "black" 
plt.rcParams['legend.fontsize'] = 12
plt.rcParams["legend.title_fontsize"] = 12
plt.rcParams["legend.facecolor"] = "white"
plt.rcParams["figure.facecolor"] = "green"
plt.rcParams["axes.labelsize"] = 20
plt.rcParams["scatter.marker"] = "*"
plt.title('Testing Graph')
plt.xlabel("X") 
plt.ylabel("Y")
plt.show()
plt.close()




# Successes expected 
assert plt.rcParams['axes.facecolor'] == "white" # Checks that the face colour is white  
assert plt.rcParams['axes.titlesize'] == 20 # Checks the title font size
assert plt.rcParams['legend.fontsize'] == 12 # Checks the legend font size of points 
assert plt.rcParams["legend.facecolor"] == "white" # Checks the legend face colour 
assert plt.rcParams["figure.facecolor"] == "green" # Checks the surrounding plot colour
assert plt.rcParams["axes.labelsize"] == 20 # Checks the axis label size 
assert plt.rcParams["scatter.marker"] == "*" #Check the shape of the scatter points 
assert plt.rcParams["lines.color"] == "red"

# Fails expected 
assert plt.rcParams['axes.edgecolor'] == "blue" # Checks that the face colour is white  
assert plt.rcParams['axes.titlesize'] == 18 # Checks the title font size
assert plt.rcParams['axes.labelsize'] == 1 # Checks the graph title font size
assert plt.rcParams["legend.title_fontsize"] == 45 #Checks the title font size of legend 

    



