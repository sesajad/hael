from django.urls import path, include
from profiles import views


urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/login/', views.login, name='login'),
    path('accounts/logout/', views.logout, name='logout'),
    path('accounts/register/', views.register, name='register'),
]
