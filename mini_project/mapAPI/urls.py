from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.main_test),
    path('path_search/', views.path_search)
]
