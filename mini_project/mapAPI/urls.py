from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.map_test),
    path('main/',views.main_test),
    path('filter/',views.filter),
    path('link_to_Naver/',views.link_to_NaverMap, name="naver"),
]
