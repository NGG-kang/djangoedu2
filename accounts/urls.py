
from django.urls import path, reverse_lazy, re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('logout/', views.logout, name='logout'),
    path('login/', views.login, name='login'),
    path('password_change/', views.password_change, name='password_change'),
    path('signup/', views.signup, name='signup'),
    path('sendmail/', views.sendMail, name='sendmail'),
    path('edit/', views.profile_edit, name='profile_edit'),

    re_path(r'^(?P<username>[\w.@+-]+)/follows/$', views.user_follow, name='user_follow'),
    re_path(r'^(?P<username>[\w.@+-]+)/unfollows/$', views.user_unfollow, name='user_unfollow'),
]