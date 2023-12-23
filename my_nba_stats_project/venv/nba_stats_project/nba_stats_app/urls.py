# nba_stats_app/urls.py
from django.urls import path
from .views import HomeView
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    # Add more URL patterns as needed
]