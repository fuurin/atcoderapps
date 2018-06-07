from django.shortcuts import render
from django.views.generic import FormView
from .kernel.atcoder_figure import performance_figure
from .kernel.base64_graph import base64_png
from .forms import UserNamesForm



class IndexView(FormView):
	template_name = "index.html"
	form_class = UserNamesForm



class ShowGraphView(FormView):
	template_name = "show_graph.html"
	form_class = UserNamesForm

	def atcoder_table(self, username):
		from .kernel.atcoder_data import atcoder_data_frame
		df = atcoder_data_frame(username)
		return df.to_html() if not df.empty else "User Not Found."

	def get_context_data(self, **kwargs):
		username = self.username = self.request.GET.get("username")
		rivalname = self.rivalname = self.request.GET.get("rivalname")
		context = super().get_context_data(**kwargs)
		context['username'], context['rivalname'] = username, rivalname	
		context['figure'] = base64_png(performance_figure(username, rivalname))
		return context

	def get_form(self):
		form = super(ShowGraphView, self).get_form()
		form.set_username_value(self.username)
		form.set_rivalname_value(self.rivalname)
		return form