import pytest
import matplotlib.pyplot as plt
import numpy as np

# The following tests work for all three themes as these tests are scanning through the elements within the themes
# but the framework of three themes remain the same.

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



def test_facecolor():
    ''' A function that checks the face colour of the plot background  '''
    
    assert plt.rcParams['axes.facecolor'] == "white"  


def test_title_size():
    '''A function that checks that the title font size of a graph '''
    
    assert plt.rcParams['axes.titlesize'] == 20 

    
def test_legend_fontsize():    
    ''''A function that checks that the font size of the legend title of a graph  '''
    
    assert plt.rcParams['legend.fontsize'] == 12 

    
def test_legend_facecolor():   
    ''' 'A function that checks the legend face colour of a graph '''
    
    assert plt.rcParams["legend.facecolor"] == "white"  

    
def test_figure_facecolor():    
    ''' A function that checks the plot's surrounding colour of a graph ''' 
    
    assert plt.rcParams["figure.facecolor"] == "green" 

    
def test_axes_labelsize():    
    ''' A function that checks the label fond size of the axis titles'''
    
    assert plt.rcParams["axes.labelsize"] == 20 


def test_scatter_marker():    
    '''A function that checks the shape of the scatter points '''
    
    assert plt.rcParams["scatter.marker"] == "*"  


# Fails expected 


def test_axes_edgecolor():    
    ''' A function that checks the edge colours of the axis  '''
    
    assert plt.rcParams['axes.edgecolor'] == "blue"  
  
    
def test_legend_fontsize_neg():    
    ''' A function that tests the label font size of the axis titles, that should fail''' 
    
    assert plt.rcParams['axes.labelsize'] == 1 


def test_legend_title_fontsize():    
    ''' A test that checks the title font size of legend '''
    
    assert plt.rcParams["legend.title_fontsize"] == 45 
    
def test_title_size_neg():
    '''A test that checks that the title font size of a graph, that should fail  '''
     
    assert plt.rcParams['axes.titlesize'] == 18 

