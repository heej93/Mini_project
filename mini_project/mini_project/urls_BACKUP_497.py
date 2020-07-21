from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('main/', admin.site.urls),
=======
    path('map/', include('map.urls'))
>>>>>>> origin/kakao_API
]
