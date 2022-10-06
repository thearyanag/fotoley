from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('' , views.dashboard, name='dashboard'),
    path('profile_list/', views.profile_list, name='profile_list'),
    path('profile/<int:pk>/', views.profile_detail, name='profile_detail'),
]
