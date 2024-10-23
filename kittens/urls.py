from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('types/', views.types, name='types'),
    path('care/', views.care, name='care'),
    path('photos/', views.photos, name='photos'),
]
