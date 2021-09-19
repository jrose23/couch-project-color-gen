from django.urls import path
from . import views

urlpatterns = [
    path('', views.random_color, name='random_color'),
    path('<str:color>', views.custom_color, name='custom_color'),
]
