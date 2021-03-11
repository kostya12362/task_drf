from django.urls import path, include
from rest_framework import routers
from event.views import EventViewSet, CreateUserView
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register('event', EventViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('registration/', CreateUserView.as_view()),
    path('login/', obtain_auth_token),
]