import matplotlib
matplotlib.use('agg') # async handler deleted by the wrong thread を防ぐ

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from .atcoder_data import atcoder_data_frame



AREA_COLOR = [
	[4000, 6000, 'tomato'],
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



def upper_lower_bounds(x, upper, lower, color=None, alpha=None):
	xlength = len(x)
	
	y_upper = np.full(xlength, upper)
	y_lower = np.full(xlength, lower)
	
	plt.fill_between(x, y_upper, y_lower, facecolor=color, alpha=alpha)



def atcoder_color_fill(x_area):
	for ac in AREA_COLOR: 
		upper_lower_bounds(x_area, ac[0], ac[1], ac[2], ALPHA)



def find_upper_limit(p_max):
	for i, ac in enumerate(AREA_COLOR):
		if ac[1] <= p_max and p_max < ac[0]:
			break
			
	if i == 0:
		return AREA_COLOR[i][0]
	else: 
		return AREA_COLOR[i-1][0]



def plot_user_performance(ax, username):
	dataframe = atcoder_data_frame(username)

	if dataframe.empty: return False

	df = dataframe[dataframe.IsRated]
	x = np.array(pd.to_datetime(df.EndTime))
	y = df.InnerPerformance
	
	ax.plot(x, y, label=username)
	
	user_ylim = find_upper_limit(y.max())
	max_ylim = max(ax.get_ylim()[1], user_ylim)
	ax.set_ylim(0, max_ylim)
	
	return True



def performance_figure(username=None, rivalname=None):
	fig, ax = plt.subplots(figsize=(8,6))

	user_exist, rival_exist = False, False
	if username: user_exist = plot_user_performance(ax, username)
	if rivalname: rival_exist = plot_user_performance(ax, rivalname)

	if user_exist and rival_exist:
		plt.title("Performance of {} and {}".format(username, rivalname))
	elif user_exist:
		plt.title("Performance of {}".format(username))
	elif rival_exist:
		plt.title("Performance of {}".format(rivalname))
	else:
		plt.title("Both users could not be found.")

	atcoder_color_fill(ax.get_xlim())

	plt.xlabel("time")
	plt.ylabel("performance")
	plt.legend()
	plt.grid()
	plt.close()

	fig.autofmt_xdate() # 時系列ラベルが重ならないようにする
	return fig