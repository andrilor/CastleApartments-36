from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index-forsida"),
    path('<int:id>', views.get_eign_by_id, name="eignir"),
    path('<int:id>', views.get_starfsmenn_by_id, name="starfsmenn_upplisingar")
]
