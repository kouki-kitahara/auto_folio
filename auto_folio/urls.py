from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('user/<int:pk>/', views.user_show, name='user_show'),
    path('user/new', views.user_new, name='user_new'),
]
