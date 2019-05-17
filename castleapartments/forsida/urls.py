from django.urls import path
from . import views
from eignir import views as view_eignir

urlpatterns = [
    path('', views.index, name = "index-forsida"),
    path('', view_eignir.index, name = "index-eignir"),
    path('<int:id>', views.get_eign_by_id, name="eignir"),
    path('<int:id>', views.get_starfsmenn_by_id, name="starfsmenn_upplisingar")
]
