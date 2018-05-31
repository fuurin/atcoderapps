from django.shortcuts import render
from django.views.generic import FormView
import matplotlib.pyplot as plt
from .kernel.atcoder_figure import performance_figure_by_username
from .kernel.base64_graph import base64_png
from .forms import UserNameForm

class IndexView(FormView):
	template_name = "index.html"
	form_class = UserNameForm


class ShowGraphView(FormView):
	template_name = "show_graph.html"
	form_class = UserNameForm

	def atcoder_table(self, username):
		from .kernel.atcoder_data import atcoder_data_frame
		df = atcoder_data_frame(username)
		return df.to_html() if not df.empty else "User Not Found."

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		if self.request.GET.get("username"):
			username = self.request.GET["username"]
			figure = performance_figure_by_username(username)		
			context['atcoder_graph'] = base64_png(figure)
			# context['atcoder_data_table'] = self.atcoder_table(username)
		return context