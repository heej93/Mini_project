from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', ),
    path('map/', include('map.urls'),)
]
