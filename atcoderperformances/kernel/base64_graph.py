from io import BytesIO
import base64

def base64_png(matplot_figure):
	buff = BytesIO()
	matplot_figure.canvas.print_png(buff)
	base64_data = base64.b64encode(buff.getvalue())
	return str(base64_data)[2:-1]