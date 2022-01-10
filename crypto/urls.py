from django.urls import path, include
from . import views

app_name = 'crypto'

urlpatterns = [
    path('', views.home, name='home')
]