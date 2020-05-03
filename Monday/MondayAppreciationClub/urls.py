from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ticker, name="ticker"),
    path('newsinfo/', views.news_info, name='newsinfo'),
    path('stockinfo/', views.lookup_info, name='stockinfo'),
]