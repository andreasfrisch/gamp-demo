from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('newest/', views.newest, name='newest')
]

