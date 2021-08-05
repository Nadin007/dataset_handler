from django.urls import include, path
from rest_framework import routers

from .views import ShopsDBViewSet

router = routers.DefaultRouter()
router.register(r'metrics', ShopsDBViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt'))
]
