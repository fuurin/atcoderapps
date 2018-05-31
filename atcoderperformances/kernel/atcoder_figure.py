import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from .atcoder_data import atcoder_data_frame

def performance_figure(dataframe):
	df = dataframe[dataframe.IsRated]
	x = pd.to_datetime(df.EndTime)
	y = df.InnerPerformance

	figure = plt.plot(x, y)[0].figure
	figure.autofmt_xdate() # 時系列ラベルが重ならないようにする
	
	plt.close()
	return figure

def performance_figure_by_username(username):
	data = atcoder_data_frame(username)
	return performance_figure(data)