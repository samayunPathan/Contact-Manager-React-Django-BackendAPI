from django.urls import path
from rest_framework.routers import DefaultRouter
from contactAPI.views import UserProfileViewSet,ContactViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router=DefaultRouter()
router.register(f'user',UserProfileViewSet)
router.register(f"contact",ContactViewSet,basename="contact")


urlpatterns = [path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),]+router.urls

