
<img src="/img/CB8new.png" width="200" align = "right">

# Colourblind8

A python package that creates colourblind friendly themes.

### Authors

| [Ian Flores](https://github.com/ian-flores) | [Sabrina Tse](https://github.com/sabrinatkk) | [Hayley Boyce](https://github.com/hfboyce)
|:------------:|:--------------:|:--------------:|

### Project

**Overview**

`Colourblind8` will be a brand new theme package implemented for `matplotlib` to optimize graphs into a format interpretable by people with colourblindness. Colourblindness, also known as colour vision deficiency, is a condition that affects individuals how they perceive colours visually. According to [colourblindawareness.org](http://www.colourblindawareness.org/colour-blindness/), colourblindness affects 1 in every 12 men and 1 in every 200 women globally. The package is inspired by the fact that people without knowledge about this condition don't know how to make their graphs accesible. Our objective is to enhance data visualization by implementing proper colours so that the graphs are perceived correctly by all readers as intended.

**Scope**

At this stage, `Colourblind8` will focus on developing settings for the three most prevalent colourblind perspectives - protanopia, deuteranopes and tritanopes (see Appendix for more information on the types of colourblindness). 


### Functions Included In This Package

- `set_deutera()`:
  - This function implements a theme that makes plots accesible to people with deuteranopia. It modifies the colour of geometric objects (points, lines, etc) and the layout of the plot.
- `set_prota()`
  - This function implements a theme that makes plots accesible to people with protanopia. It modifies the colour of geometric objects (points, lines, etc) and the layout of the plot.
- `set_trita()`
  - This function implements a theme that makes plots accesible to people with tritanopia. It modifies the colour of geometric objects (points, lines, etc) and the layout of the plot.
  
  
### Installation 


To install `Colourblind8`, please input the following into the Terminal:

```pip install git+https://github.com/UBC-MDS/Colourblind8.git```


### Usage 

#### Function example 



### Our Package in the Python Ecosystem 

To the best of our knowledge, there is currently no other colourblind specific package available for matplotlib that offers colourblind-friendly palettes or themes. `Seaborn`, in conjunction with `matplotlib`, offers a single default colour palette ([source](https://seaborn.pydata.org/tutorial/color_palettes.html)) named `colorblind` targeting readers with general colourblindness and does not accommodate different variants of colourblind conditions.

`Colourblind8` will bridge the gap as it attempts to fit into the Python ecosystem by offering a convenient and effective way to give all matplotlib visualizations a theme and fully inclusive colour palette.  A package that shows a similar contribution to the python ecosystem is [`daltonize`](https://github.com/joergdietrich/daltonize). This package aids to creating all images colourblind friendly as opposed to `Colourblind8` which will make specifically data visualizations, plots and graphs fully inclusive for all readers.

### Appendix

Protanopia

Protanopes are more likely to confuse:-
1. Black with many shades of red
2. Dark brown with dark green, dark orange and dark red
2. Some blues with some reds, purples and dark pinks
3. Mid-greens with some oranges

Deuteranopes

Deuteranopes are more likely to confuse:-
1. Mid-reds with mid-greens
2. Blue-greens with grey and mid-pinks
3. Bright greens with yellows
4. Pale pinks with light grey
5. Mid-reds with mid-brown
6. Light blues with lilac

Tritanopes

The most common colour confusions for tritanopes are light blues with greys, dark purples with black, mid-greens with blues and oranges with reds. 

source:http://www.colourblindawareness.org/colour-blindness/types-of-colour-blindness/

-------------------------------------------------------
http://www.colourblindawareness.org/colour-blindness/

