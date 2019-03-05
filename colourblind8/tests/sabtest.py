import matplotlib.pyplot as plt
from colourblind8.colourblind8 import Colourblind8
import numpy as np
import pytest

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

cb = Colourblind8()


def test_input_values():
    '''tests input parameters are correct sizes'''
    with pytest.raises(ValueError):

        # Expect ERROR if the length of two vectors are different
        cb.plot_scatter(x,y_wrong_size,alpha =1.0,
              labels =['a','b','c','d','e','f','g','h','i'],
              palette = 'deutera',
              title = "Deutera Line Example",
              x_lab = "X label" ,
              y_lab = "Y label" ,
              legend_title = "Legend")

        #Expect ERROR if alpha is outside range
        cb.plot_scatter(nonlist_x,y_list,alpha =5.0,
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

        cb.plot_scatter(nonlist_x,nonlist_y,alpha ="1.0",
              labels =['a','b','c','d','e','f','g','h','i'],
              palette = 'deutera',
              title = "Deutera Line Example",
              x_lab = "X label" ,
              y_lab = "Y label" ,
              legend_title = "Legend")

def test_input(x,y ,alpha, labels, palette, title, x_lab, y_lab, legend_title):
    '''tests input parameters are correct types and in correct range '''

    assert type(x) == list
    assert type(y) == list
    assert type(labels) == list
    assert type(palette) == str
    assert type(title) == str
    assert type(x_lab) == str
    assert type(y_lab) == str
    assert type(legend_title) == str
    assert type(alpha) == float
    assert alpha <= 1.0
    assert alpha >= 0.0
    assert len(y) == len(labels)
