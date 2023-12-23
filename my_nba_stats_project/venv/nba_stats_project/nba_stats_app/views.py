# nba_stats_app/views.py
from django.shortcuts import render
from django.views.generic import TemplateView
def index(request):
    # Your view logic goes here
    return render(request, 'nba_stats_app/home.html')
class HomeView(TemplateView):
    template_name = 'nba_stats_app/home.html'






