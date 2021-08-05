from db_handler.models import ShopsDB
from rest_framework import filters


class DateFilter(filters.SearchFilter):

    def filter_queryset(self, request, queryset, view):
        search_terms = request.GET

        if (search_terms.get('from_date') is not None
           and search_terms.get('date_to') is not None):
            queryset = ShopsDB.objects.filter(date__range=(
                search_terms['from_date'], search_terms['date_to']))

        if (search_terms.get('from_date') is not None
           and search_terms.get('date_to') is None):
            queryset = ShopsDB.objects.filter(
                date__gte=search_terms['from_date'])

        if (search_terms.get('date_to') is not None
           and search_terms.get('from_date') is None):
            queryset = queryset.filter(date__lte=search_terms['date_to'])
        return queryset


'''class GroupFilterMixin(object):

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
            result[key].append(serializers.serialize('json', [shop]))
        return result
'''
