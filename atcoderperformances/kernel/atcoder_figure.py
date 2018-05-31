import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from .atcoder_data import atcoder_data_frame

AREA_COLOR = [
	[4000, 2800, 'tomato'],
	[2800, 2400, 'sandybrown'],
	[2400, 2000, 'yellow'],
	[2000, 1600, 'mediumpurple'],
	[1600, 1200, 'lightskyblue'],
	[1200, 800, 'lightgreen'],
	[800, 400, 'peru'],
	[400, 0, 'darkgrey']
]

ALPHA = 0.7

def upper_lower_bounds(plt, x, upper, lower, color=None, alpha=None):
	xlength = len(x)
	y_upper = np.full(xlength, upper)
	y_lower = np.full(xlength, lower)
	plt.fill_between(x, y_upper, y_lower, facecolor=color, alpha=alpha)

def find_limit(p_max):
	for i, ac in enumerate(AREA_COLOR):
		if ac[1] <= p_max and p_max < ac[0]:
			return i if i == 0 else i-1

def performance_figure(dataframe, username=None):
	df = dataframe[dataframe.IsRated]
	x = np.array(pd.to_datetime(df.EndTime))
	y = df.InnerPerformance

	plt.figure(figsize=(10,8))
	if username: plt.title("{}'s performance @ atcoder".format(username))
	plt.ylim(0, AREA_COLOR[find_limit(y.max())][0])
	for ac in AREA_COLOR: upper_lower_bounds(plt, x, ac[0], ac[1], ac[2], ALPHA)
	plt.xlabel("time")
	plt.ylabel("performance")
	plt.grid()
	figure = plt.plot(x, y)[0].figure
	figure.autofmt_xdate() # 時系列ラベルが重ならないようにする

	plt.close()
	return figure

def performance_figure_by_username(username):
	data = atcoder_data_frame(username)
	return performance_figure(data, username)