from django.urls import path, include

from profiles import views


urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/register/', views.register, name='register'),
]
