from django.urls import path, include
from . import views

urlpatterns = [
    path('newsinfo/', views.news_info, name='newsinfo'),
    path('stockinfo/', views.lookup_info, name='stockinfo'),
]