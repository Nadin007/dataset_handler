from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination

from db_handler.models import ShopsDB, User
from .filters import DateFilter, GroupFilterMixin
from .serializers import ShopsDBSerializer, UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ShopsDBViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = ShopsDB.objects.all()
    serializer_class = ShopsDBSerializer
    pagination_class = PageNumberPagination
    filter_backends = (
        DateFilter, DjangoFilterBackend, OrderingFilter, GroupFilterMixin)
    ordering_fields = ('date', 'shop', 'country', 'visitors', 'earnings')
