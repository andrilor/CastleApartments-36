from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordResetDoneView
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
    path('password_reset/', PasswordResetView.as_view(template_name='user/gleymt_lykilord.html'),name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='user/nytt_lykilord.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'), name='password_reset_complete'),
]