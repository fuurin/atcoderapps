from django.shortcuts import render
from django.views.generic import FormView			
from .kernel.atcoder_data import atcoder_data_frame
from .kernel.html_graph import atcoder_graph
from .forms import UserNameForm

class IndexView(FormView):
	template_name = "index.html"
	form_class = UserNameForm


class ShowGraphView(FormView):
	template_name = "show_graph.html"
	form_class = UserNameForm

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		if self.request.GET.get("username"):
			username = self.request.GET["username"]
			df = atcoder_data_frame(username)
			context['atcoder_data_table'] = df.to_html() if not df.empty else "User Not Found."
		return context