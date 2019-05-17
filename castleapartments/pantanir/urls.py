from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.index, name='index-pantanir'),
    path('stadfesta/<int:id>', views.stadfesta, name="stadfesta"),
    path('kvittun/<int:id>', views.kvittun, name="kvittun"),
]