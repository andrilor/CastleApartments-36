from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index-opinhus"),
    path('<int:id>', views.check_if__opinhus_exists_by_eign, name="opinhus")
]