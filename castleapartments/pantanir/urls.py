from django.urls import path
from . import views

urlpatterns = [
    path('pantanir', views.index, name='index-pantanir'),
]
