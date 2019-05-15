from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index-eignir"),
    path('<int:id>', views.uppl_um_eign, name="eignir"),
    path('sorted-name', views.alphebeticallySortedEign, name='sorted-name'),
    path('sorted-price', views.priceSortedEign, name='sorted-price')
]
