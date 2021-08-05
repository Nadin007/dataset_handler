from collections import OrderedDict
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
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

    def list(self, request, *args, **kwargs):
        search_terms = self.request.GET
        if (search_terms.get('group') is not None
           and search_terms.get('group') == 'shop'):
            return Response(OrderedDict(self._build_shop_list()))
        return super().list(request, *args, **kwargs)

    def _build_shop_list(self):
        shops = ShopsDB.objects.all()
        result = {}
        for shop in shops:
            key = shop.shop
            if key not in result:
                result[key] = []
            result[key].append(ShopsDBSerializer(
                shop, context={'request': self.request}).data)
        return result
