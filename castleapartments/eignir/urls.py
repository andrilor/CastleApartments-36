from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index-eignir"),
    path('<int:id>', views.get_eign_by_id, name="eignir")
]
