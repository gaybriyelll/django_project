from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('breeds/', views.breeds, name='breeds'),
    path('facts/', views.facts, name='facts'),
    path('gallery/', views.gallery, name='gallery'),
]
