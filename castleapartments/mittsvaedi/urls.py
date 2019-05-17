from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index-mittsvaedi"),
    path('<int:id>', views.get_profile_by_id, name="profile"),
    path('leitarsaga', views.leitar_saga, name="leitarsaga")
]
