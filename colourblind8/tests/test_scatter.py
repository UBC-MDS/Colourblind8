import pytest
import matplotlib.pyplot as plt
import numpy as np
from Colourblind8.Colourblind8 import Colourblind8

# The following tests work for all three themes as these tests are scanning through the elements within the themes
# but the framework of three themes remain the same.

cb = Colourblind8()

# create some Testing Data
nonlist_x = 11
nonlist_y = 22


x=[1,2,4,5]
y_wrong_size = [1,5,6,3,6]

y_list=[[1,2,3.3,2.2],
        [2,3,3.5,4],
        [3,3.6,4.3,4],
        [4,4.2,5,5.6],
        [5,5.5,5.2,6.5],
        [6,7.2,6.1,6.9],
        [7,8,7.4,8],
        [8,9,7.8,8.2],
        [9,9.3,9.6,9.2]]


## Testing Function Input
def test_input_values():
    '''tests input parameters are correct sizes'''
    with pytest.raises(ValueError):

        # Expect ERROR if the length of two vectors are different
        cb.plot_lines(x,y_wrong_size,alpha =1.0,
              labels =['a','b','c','d','e','f','g','h','i'],
              palette = 'deutera',
              title = "Deutera Line Example",
              x_lab = "X label" ,
              y_lab = "Y label" ,
              legend_title = "Legend")

        #Expect ERROR if alpha is outside range
        cb.plot_lines(nonlist_x,y_list,alpha =5.0,
              labels =['a','b','c','d','e','f','g','h','i'],
              palette = 'deutera',
              title = "Deutera Line Example",
              x_lab = "X label" ,
              y_lab = "Y label" ,
              legend_title = "Legend")


def test_input_index():
    '''tests input parameters are consistent lengths'''
    with pytest.raises(IndexError):
        #Expect ERROR if labels length is inconsistent with y length
        cb.plot_scatter(x,y_list,alpha =1.0,
              labels =['a','b'],
              palette = 'deutera',
              title = "Deutera Line Example",
              x_lab = "X label" ,
              y_lab = "Y label" ,
              legend_title = "Legend")


def test_input_types():
    '''tests input parameters are correct types'''
    with pytest.raises(TypeError):

        # Expect ERROR if any of the parameters are not expected type
        cb.plot_scatter(x,nonlist_y,alpha =1.0,
              labels =['a','b','c','d','e','f','g','h','i'],
              palette = 'deutera',
              title = "Deutera Line Example",
              x_lab = "X label" ,
              y_lab = "Y label" ,
              legend_title = "Legend")

        cb.plot_scatter(nonlist_x,y_list,alpha ="1.0",
              labels =['a','b','c','d','e','f','g','h','i'],
              palette = 'deutera',
              title = "Deutera Line Example",
              x_lab = "X label" ,
              y_lab = "Y label" ,
              legend_title = "Legend")

## Testing Function Output

def test_num_geoms():
    '''A function that checks that the functions returns the correct number of
       geom objects given an input.
    '''
    scatter_plot = cb.plot_scatter(x, y_list, palette = 'deutera')
    num_geoms = scatter_plot.get_children()
    assert len(num_geoms) == 19

def test_labels():
    '''A function that checks that the functions returns the correct labels'''
    scatter_plot = cb.plot_scatter(x, y_list,
    palette = 'deutera',
    x_lab = 'axis_x',
    y_lab = 'axis_y',
    title = 'axis_title')

    assert scatter_plot.get_xlabel() == 'axis_x'
    assert scatter_plot.get_ylabel() == 'axis_y'
    assert scatter_plot.get_title() == 'axis_title'

def test_legend():
    '''A function that checks that the legend assignment inside the function works'''
    scatter_plot = cb.plot_scatter(x,
    y_list,
    palette = 'deutera',
    labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9'])
    class_legend = str(type(scatter_plot.get_legend()))

    assert class_legend == "<class 'matplotlib.legend.Legend'>"
