from django.urls import path
from .views import IndexView, ShowGraphView

urlpatterns = [
	path('', IndexView.as_view(), name='index'),
	path('show_graph/', ShowGraphView.as_view(), name='show_graph'),
]