import pytest
import matplotlib.pyplot as plt
import numpy as np
from colourblind8.colourblind8 import Colourblind8

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

alpha = .4
bins = 30 
labels =['a','b','c','d','e','f','g','h','i']
palette = 'trita' 
title = 'Test' 
x_lab = " x  value "
legend_title = "Legend test "

## Testing Function Input
def test_input_values():
    '''tests input parameters are correct sizes'''
    with pytest.raises(ValueError):

        #Expect ERROR if alpha is outside range
        cb.plot_histogram(y_list, alpha =5.0,bins = 10,
              labels =['a','b','c','d','e','f','g','h','i'],
              palette = 'deutera',
              title = "Deutera Line Example",
              x_lab = "X label" ,
              legend_title = "Legend")

        cb.plot_histogram(y_list, alpha =5.0,bins = 0.3,
              labels =['a','b','c','d','e','f','g','h','i'],
              palette = 'deutera',
              title = "Deutera Line Example",
              x_lab = "X label" ,
              legend_title = "Legend")

        cb.plot_histogram(y_list, alpha =1.0, bins ="10",
              labels =['a','b','c','d','e','f','g','h','i'],
              palette = 'deutera',
              title = "Deutera Line Example",
              x_lab = "X label" ,
              legend_title = "Legend")


def test_input_types():
    '''tests input parameters are correct types'''
    with pytest.raises(TypeError):

        # Expect ERROR if any of the parameters are not expected type
        cb.plot_histogram(y_wrong_size, alpha = [1.0], bins =10,
              labels =['a','b','c','d','e','f','g','h','i'],
              palette = 'deutera',
              title = "Deutera Line Example",
              x_lab = "X label" ,
              legend_title = "Legend")
        
def test_input( ):
    '''tests input parameters are correct types and in correct range '''
    
    assert type(y_list) == list
    assert type(labels) == list
    assert type(bins) == int 
    assert type(palette) == str
    assert type(title) == str
    assert type(x_lab) == str
    assert type(legend_title) == str
    assert type(alpha) == float
    assert alpha <= 1.0
    assert alpha >= 0.0
    assert len(y_list) == len(labels)
    assert bins > 0

## Testing Function Output

def test_num_geoms():
    '''A function that checks that the functions returns the correct number of
       geom objects given an input.
    '''
    hist_plot = cb.plot_histogram(y_list, palette = 'deutera')
    num_geoms = hist_plot.get_children()
    assert len(num_geoms) == 100

def test_labels():
    '''A function that checks that the functions returns the correct labels'''
    hist_plot = cb.plot_histogram(y_list,
    palette = 'deutera',
    x_lab = 'axis_x',
    title = 'axis_title')

    assert hist_plot.get_xlabel() == 'axis_x'
    assert hist_plot.get_ylabel() == 'Frequency'
    assert hist_plot.get_title() == 'axis_title'

def test_legend():
    '''A function that checks that the legend assignment inside the function works'''
    hist_plot = cb.plot_histogram(
    y_list,
    palette = 'deutera',
    labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9'])
    class_legend = str(type(hist_plot.get_legend()))

    assert class_legend == "<class 'matplotlib.legend.Legend'>"
