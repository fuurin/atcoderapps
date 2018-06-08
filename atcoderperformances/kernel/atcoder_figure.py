import matplotlib
matplotlib.use('agg') # async handler deleted by the wrong thread を防ぐ

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from .atcoder_data import atcoder_data_frame



AREA_COLOR = [
	[5000, 4000, 'tomato'],
	[4000, 2800, 'tomato'],
	[2800, 2400, 'sandybrown'],
	[2400, 2000, 'yellow'],
	[2000, 1600, 'royalblue'],
	[1600, 1200, 'lightskyblue'],
	[1200, 800, 'lightgreen'],
	[800, 400, 'peru'],
	[400, 0, 'darkgrey']
]

ALPHA = 0.7



def entitle(exist_user, exist_rival):
	if len(exist_user) and len(exist_rival):
		if len(exist_rival) == 1:
			title = "Performance of {} and {}".format(exist_user[0], exist_rival[0])
		else:
			title = "Performance of {} and rivals".format(exist_user[0])
	
	elif len(exist_user):
		title = "Performance of {}".format(exist_user[0])
	
	elif len(exist_rival):
		if len(exist_rival) == 1:
			title = "Performance of {}".format(exist_rival[0])
		else:
			title = "Performance of rivals"
	
	else:
		title = "All users could not be found."

	return title



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



def plot_user_performance(ax, users):
	exist_user = []
	
	for user in users:
		dataframe = atcoder_data_frame(user)

		if dataframe.empty: continue

		df = dataframe[dataframe.IsRated]
		x = np.array(pd.to_datetime(df.EndTime))
		y = df.InnerPerformance
		
		ax.plot(x, y, label=user, marker="o")
		
		user_ylim = find_upper_limit(y.max())
		max_ylim = max(ax.get_ylim()[1], user_ylim)
		ax.set_ylim(0, max_ylim)

		exist_user.append(user)

	return exist_user



def performance_figure(username=None, rivalnames=None):
	fig, ax = plt.subplots(figsize=(8,6))

	exist_user, exist_rival = [], []
	if username: 
		exist_user = plot_user_performance(ax, [username])
	if rivalnames: 
		exist_rival = plot_user_performance(ax, rivalnames)

	not_found_users = list((set([username]) - set(exist_user)) | (set(rivalnames) - set(exist_rival)))
	
	atcoder_color_fill(ax.get_xlim())

	title = entitle(exist_user, exist_rival)
	plt.title(title, fontsize=20)
	plt.xlabel("date")
	plt.ylabel("performance")
	plt.legend()
	plt.grid()
	plt.tight_layout()
	plt.close()

	fig.autofmt_xdate() # 時系列ラベルが重ならないようにする
	return fig, not_found_users