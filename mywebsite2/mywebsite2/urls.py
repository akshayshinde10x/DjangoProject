from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('abouts/', views.about, name='introduction'),
    path('abouts/details/', views.details),
]
