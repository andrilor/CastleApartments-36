from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name="register"),
    path('login', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='/'), name='logout'),
    path('profile', views.profile, name='profile'),
    path('newUserProfile', views.newUser, name = 'newUserProfile'),
    path('newUserUpplysingar', views.newUser_upplysingar, name = 'newUserUpplysingar'),
    #path('profile/<username>/', views.logout, name='logout'),
    #url(r'^profile_view/(?P<username>\w+)/$', views.logout, name='logout'),
]