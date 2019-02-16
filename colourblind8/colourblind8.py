import matplotlib.pyplot as plt

class Colourblind8:

    def __init__(self):
        self.deutera_colours =  ['#666E95', '#FFC13D', '#2F86E5', '#ACA6C3', '#483E3C',
                                 '#E8C6BA', '#867065', '#005186', '#B0860F', '#FFD9B0']


        self.prota_colours = ['#7D7C01', '#59709E', '#4C5631', '#3F59E8', '#BDBB64',
                              '#35A9E0', '#E8E602', '#C1C1C7', '#0E1079']

        self.trita_colours = ['#5F727A', '#FFB7C2', '#01919A', '#A8A8B4', '#BDE6F4',
                              '#4A3F45', '#B77B87', '#00585C', '#932929']

        plt.rcParams['axes.titlesize'] = 20
        plt.rcParams['axes.edgecolor'] = "black"
        plt.rcParams['legend.fontsize'] = 10
        plt.rcParams["legend.facecolor"] = "white"
        plt.rcParams["figure.facecolor"] = "white"
        plt.rcParams["axes.labelsize"] = 16

    def plot_scatter(self, x, y, alpha = 1,  labels = None, palette = None,
                title = None, x_lab = None, y_lab = None, legend_title = None):

        # Checks colour palette
        if palette == 'deutera':
                colours = self.deutera_colours
        elif palette == 'trita':
                colours = self.trita_colours
        elif palette == 'prota':
                colours = self.prota_colours

        fig, ax = plt.subplots()

        if labels:
            for idx, values in enumerate(y):
                ax.scatter(x,
                          values,
                          color = colours[idx],
                          alpha = alpha,
                          label = labels[idx])
        else:
            for idx, values in enumerate(y):
                ax.scatter(x,
                           values,
                           color = colours[idx],
                           alpha = alpha)

        if title:
            ax.set_title(title)

        if x_lab:
            ax.set_xlabel(x_lab)

        if y_lab:
            ax.set_ylabel(y_lab)

        ax.legend(title = legend_title, bbox_to_anchor=(1.01, 1), loc = "upper left")
        return ax
    
    def plot_histogram(self, y, alpha = 1.0, labels = None, palette = None, 
                title = None, x_lab = None, legend_title = None):
    
        # Checks colour palette
        if palette == 'deutera':
                colours = self.deutera_colours
        elif palette == 'trita':
                colours = self.trita_colours
        elif palette == 'prota':
                colours = self.prota_colours

        fig, ax = plt.subplots()
 
    
        if labels:
            for idx, values in enumerate(y):
                ax.hist(values,
                        edgecolor = 'white',
                        linewidth=1, 
                        alpha = alpha,
                        color = colours[idx],
                        label = labels[idx])
        else:
            for idx, values in enumerate(y):
                ax.hist(x, 
                           values,
                           edgecolor = 'white', 
                           linewidth=1,
                           alpha = alpha,
                           color = colours[idx])

        if title:
                ax.set_title(title)

        if x_lab:
                ax.set_xlabel(x_lab)
           
        ax.set_ylabel("Frequency")
        ax.legend(title = legend_title, bbox_to_anchor=(1.01, 1),  loc="upper left")

        return ax
    
