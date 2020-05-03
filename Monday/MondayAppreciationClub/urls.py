from django.urls import path, include
from . import views

urlpatterns = [
    path('newsinfo/', views.news_info, name='send_json'),
]