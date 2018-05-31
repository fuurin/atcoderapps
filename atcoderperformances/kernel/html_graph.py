import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
from django.http import HttpResponse
import numpy as np

def draw_performance_graph(data):
	fig, ax = plt.subplots()
	ax.set_title('SIN GRAPH')
	x = np.arange(0, 5, 0.01)
	y = np.sin(x)
	ax.plot(x, y)
	return fig

def make_png_response(fig):
	canvas = FigureCanvasAgg(fig)
	response = HttpResponse(content_type='image/png')
	canvas.print_png(response)
	return response

def atcoder_graph(data):
	fig = draw_performance_graph([])
	image = make_png_response(fig)
	plt.close()
	return image