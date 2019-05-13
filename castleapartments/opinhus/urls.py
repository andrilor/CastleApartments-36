from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index-opinhus"),
    path('<int:id>', views.get_opinhus_by_id, name="opinhus")
]