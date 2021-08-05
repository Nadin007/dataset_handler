from rest_framework.filters import OrderingFilter
from db_handler.models import User, ShopsDB
from .serializers import UserSerializer, ShopsDBSerializer
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .filters import DateFilter
from django_filters.rest_framework import DjangoFilterBackend


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ShopsDBViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = ShopsDB.objects.all()
    serializer_class = ShopsDBSerializer
    pagination_class = PageNumberPagination
    filter_backends = (DateFilter, DjangoFilterBackend, OrderingFilter)
    ordering_fields = ('date', 'shop', 'country', 'visitors', 'earnings')
