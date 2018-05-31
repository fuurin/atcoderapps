import numpy as np
import matplotlib.pyplot as plt
from .atcoder_data import atcoder_data_frame

def performance_figure(data):
	x = np.arange(0, 5, 0.01)
	y = np.sin(x)
	figure = plt.plot(x, y)[0].figure
	return figure