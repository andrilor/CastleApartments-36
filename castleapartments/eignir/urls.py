from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index-eignir"),
    path('<int:id>', views.uppl_um_eign, name="eignir"),
    path('sorted-name-desc', views.alphebeticallySortedEignDesc, name='sorted-name-desc'),
    path('sorted-name-asc', views.alphebeticallySortedEignAsc, name='sorted-name-asc'),
    path('sorted-price-desc', views.priceSortedEignDesc, name='sorted-price-desc'),
    path('sorted-price-asc', views.priceSortedEignAsc, name='sorted-price-asc'),
]
