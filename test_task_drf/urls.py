from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('event.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
