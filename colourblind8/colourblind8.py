import matplotlib.pyplot as plt


class Colourblind8:

	""" What is Colourblind8?

	Colourblind8 provides an improved version of matplotlib scatterplot,lineplot and histogram through colour and design enhancement for three types of colourblind conditions -Deuteranopia,Protanopia,Tritanopia.

	Example
	----------
	Colourblind8.plot_lines(x=x, y=y, alpha=1.0,labels =['a','b','c','d','e','f','g','h','i'], palette = 'deutera',
		        title = "My testing", x_lab = "X_test", y_lab = "Y_test", legend_title = "lengendtest");

	Usage
	----------
	- plot selection:

	Colourblind8.plot_lines()
	Colourblind8.plot_scatter()
	Colourblind8.plot_hist()

	- Colourpalette selection through `palette` argument within `plot()`:

	palette=['deutera','prota','trita']


	Parameters
	----------
	param1 x (list): a list of numeric values. Applicable to scatterplots and lineplots
	param2 y (list of lists): up to 9 y variables to plot based on the number of available colours per palette. For one list, please convert it to a list of lists.
	alpha(float): controling transparency level. Default value=1.0 , it takes any value between 0.0 and 1.0.
	labels : Optional. Labels for each object within the graph.
	palette (one palette): 'deutera', 'prota','trita'
	title: Optional. Title for the plot
	x_lab: Optional. Label for x axis
	y_lab: Optional. Label for y axis. Not applicable to histogram.
	legend_title: Optional. Legend title for legend.

	Returns
	-------
	plt

	an enhanced version of matplotlib plot is returned

	"""

	def __init__(self):

		#Initialize colour palette for Colourblind8.
		self.deutera_colours =  ['#666E95', '#FFC13D', '#2F86E5', '#ACA6C3', '#483E3C','#E8C6BA', '#867065', '#005186', '#B0860F', '#FFD9B0']
		self.prota_colours = ['#7D7C01', '#59709E', '#4C5631', '#3F59E8', '#BDBB64','#35A9E0', '#E8E602', '#C1C1C7', '#0E1079']
		self.trita_colours = ['#5F727A', '#FFB7C2', '#01919A', '#A8A8B4', '#BDE6F4','#4A3F45', '#B77B87', '#00585C', '#932929']
		#Initialize plot design for Colourblind8

		plt.rcParams['axes.titlesize'] = 20
		plt.rcParams['axes.edgecolor'] = "black"
		plt.rcParams['legend.fontsize'] = 10
		plt.rcParams["legend.facecolor"] = "white"
		plt.rcParams["figure.facecolor"] = "white"
		plt.rcParams["axes.labelsize"] = 16

	def plot_lines(self, x, y,alpha=1.0, labels = None, palette = None,title = None, x_lab = None, y_lab = None, legend_title = None):

		"""
		Colourblind8.plot_lines() produces a matplotlib linechart for x and y variables. It takes y variable only in a list of lists format, up to 9 lists within a list for plotting. Each line will be presented by one colour of the palette. *** For one list, please convert it to a list of a list.

		Example
		----------
		Colourblind8.plot_lines(x=x, y=y, alpha=0.5,labels =['a','b','c','d','e','f','g','h','i'], palette = 'deutera',
				        title = "My testing", x_lab = "X_test", y_lab = "Y_test", legend_title = "lengendtest")

		Parameters
		----------
		param1 x : a list of numeric values
		param2 y (list of lists): up to 9 y variables to plot based on the number of available colours per palette.
				For one list, please convert it to a list of a list.
		alpha(default value =1.0): transparency level, it takes any value between 0.0 and 1.0
		labels : Optional. Labels for each object within the graph.
		palette (one palette): 'deutera', 'prota','trita'
		title: Optional. Title for the plot
		x_lab: Optional. Label for x axis
		y_lab: Optional. Label for y axis
		legend_title: Optional. Legend title for legend.

		Returns
		-------
		plt

		an enhanced version of matplotlib lineplot is returned
		"""

        # Checks which colour palette is selected

		if palette == 'deutera':
			colours = self.deutera_colours
		elif palette == 'trita':
			colours = self.trita_colours
		elif palette == 'prota':
			colours = self.prota_colours

		fig, ax = plt.subplots()

		# Go through y variables and apply colours accordingly

		if labels:
			for idx, values in enumerate(y):
				ax.plot(x,
				          values,
				          color = colours[idx],
				          label = labels[idx],
					   alpha=alpha)
			ax.legend(title = legend_title, bbox_to_anchor=(1.01, 1))
		else:
			for idx, values in enumerate(y):
				ax.plot(x,
				           values,
				           color = colours[idx],
						alpha=alpha)

		# if the following parameters are entered, Colourblind8 will apply the theme
		if title:
			ax.set_title(title)

		if x_lab:
			ax.set_xlabel(x_lab)

		if y_lab:
			ax.set_ylabel(y_lab)

		return ax

	def plot_scatter(self, x, y, alpha = 1.0,  labels = None, palette = None,title = None, x_lab = None, y_lab = None, legend_title = None):

		"""
		Colourblind8.plot_scatter () produces a matplotlib scatterplot for x and y variables. It takes y variable only in a list of lists format, up to 9 lists within a list for plotting. Each scatter group will be presented by one colour of the palette. *** For one list, please convert it to a list of a list.

		Example
		---------
			Colourblind8.plot_scatter(x=x, y=y, alpha=0.5,labels =['a','b','c','d','e','f','g','h','i'], palette = 'deutera',
					            title = "My testing", x_lab = "X_test", y_lab = "Y_test", legend_title = "lengendtest")

		Parameters
		---------
			param1 x : a list of numeric values
			param2 y (list of lists): up to 9 y variables to plot based on the number of available colours per palette.
				For one list, please convert it to a list of a list.
			alpha(default value=1.0): transparency level, it takes any value between 0.0 and 1.0
			labels : Optional. Labels for each object within the graph.
			palette (one palette): 'deutera', 'prota','trita'
			title: Optional. Title for the plot
			x_lab: Optional. Label for x axis
			y_lab: Optional. Label for y axis
			legend_title: Optional. Legend title for legend.

		Returns
		-------
		plt

		an enhanced version of matplotlib scatterplot is returned
		"""

        # Checks which colour palette is selected

		if palette == 'deutera':
			colours = self.deutera_colours
		elif palette == 'trita':
			colours = self.trita_colours
		elif palette == 'prota':
			colours = self.prota_colours

		fig, ax = plt.subplots()

		# Go through y variables and apply colours accordingly

		if labels:
			for idx, values in enumerate(y):
				ax.scatter(x,
				          values,
				          color = colours[idx],
				          alpha = alpha,
				          label = labels[idx])
			ax.legend(title = legend_title, bbox_to_anchor=(1.01, 1))
		else:
			for idx, values in enumerate(y):
				ax.scatter(x,
				           values,
				           color = colours[idx],
				           alpha = alpha)
		# if the following parameters are entered, Colourblind8 will apply the theme
		if title:
			ax.set_title(title)

		if x_lab:
			ax.set_xlabel(x_lab)

		if y_lab:
			ax.set_ylabel(y_lab)

		return ax

	def plot_histogram(self, y, alpha = 1.0, bins = None, labels = None, palette = None,title = None, x_lab = None, legend_title = None):

		"""
		Colourblind8.plot_histogram() produces a matplotlib histogram for a list of lists. It takes a variable - parameter y- up to 9 lists within a list for plotting. Each histogram layer will be presented by one colour of the palette. *** For one list, please convert it to a list of a list.

		Example
		---------

			Colourblind8.plot_histogram(y=y, alpha=0.5, bins = 10, labels =['a','b','c','d','e','f','g','h','i'], palette = 'deutera',
					            title = "My testing", x_lab = "X_test", y_lab = "Y_test", legend_title = "lengendtest")

		Paramaters
		---------
			param1 y (a list of lists): up to 9 y variables to plot based on the number of available colours per palette.
				For one list, please convert it to a list of a list.
			alpha(default value=1.0): transparency level, it takes any value between 0.0 and 1.0
			bins: Optional. Will give consistent number of bins for each histogram. Without this bin sizes will differ for each layer.
			labels : Optional. Labels for each object within the graph.
			palette (one palette): 'deutera', 'prota','trita'
			title: Optional. Title for the plot
			x_lab: Optional. Label for horizontal axis
			legend_title: Optional. Legend title for legend.

		Returns
		---------
		plt

		an enhanced version of matplotlib histogram is returned

		"""
		# Checks colour palette
		if palette == 'deutera':
			colours = self.deutera_colours
		elif palette == 'trita':
			colours = self.trita_colours
		elif palette == 'prota':
			colours = self.prota_colours

		fig, ax = plt.subplots()

		# Go through y variables and apply colours accordingly

		if bins:
			if labels:

				stored_max=[]
				stored_min=[]
				for j in y_list:
					stored_max.append(max(j))
					stored_min.append(min(j))

				for idx, values in enumerate(y):
					ax.hist(values,

					        edgecolor = 'white',
					        linewidth=1,
					        alpha = alpha,
					        color = colours[idx],
					        label = labels[idx],

							bins = range(min(store_min),max(stored_max)))
				ax.legend(title = legend_title, bbox_to_anchor=(1.01, 1))
			else:
				for idx, values in enumerate(y):
					ax.hist(values, edgecolor = 'white', linewidth=1, alpha = alpha, color = colours[idx], bins =  range(min(store_min), max(stored_max)))
		else:
			if labels:
				for idx, values in enumerate(y):
					ax.hist(values,
					        edgecolor = 'white',
					        linewidth=1,
					        alpha = alpha,
					        color = colours[idx],
					        label = labels[idx])
				ax.legend(title = legend_title, bbox_to_anchor=(1.01, 1))
			else:
				for idx, values in enumerate(y):
					ax.hist(values,
					           edgecolor = 'white',
					           linewidth=1,
					           alpha = alpha,
					           color = colours[idx])

		# if the following parameters are entered, Colourblind8 will apply the theme
		if title:
			ax.legend(title = legend_title, bbox_to_anchor=(1.01, 1),  loc="upper left")
			ax.set_title(title)

		if x_lab:
				ax.set_xlabel(x_lab)

		ax.set_ylabel("Frequency")

		return ax
