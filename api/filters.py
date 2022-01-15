from django.db.models import Sum
from rest_framework import filters

from db_handler.models import ShopsDB


class DateFilter(filters.SearchFilter):

    def filter_queryset(self, request, queryset, view):
        try:
            method = request.method
            search_terms = request.GET
        except Exception as s:
            raise Exception(f'Exception: {s}')
        if method != 'GET':
            raise Exception('Must be GET method')

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
            return queryset.filter(date__lte=search_terms['date_to'])


GROUP_ARG_NAME = {'shop', 'country'}
ORD_ARG_POS = {'visitors', 'earnings', 'shop', 'country'}
ORD_ARG_NEG = {f'-{name}' for name in ORD_ARG_POS}
ORD_ARG_NAME = ORD_ARG_POS | ORD_ARG_NEG


class GroupFilterMixin(object):

    group_arg_name = 'group'
    ordering_arg_name = 'o'

    def ordering__queryset(self, ordering_include, group_include_field):
        order_name = 'earnings'
        ordering_include_field = {
            name for name in ordering_include if name} & ORD_ARG_NAME

        if ordering_include_field:
            order_name = ordering_include_field.pop()
        return ShopsDB.objects.values(
            *list(group_include_field)).annotate(earnings=Sum(
                'earnings'), visitors=Sum('visitors')).order_by(
                order_name)

    def filter_queryset(self, request, queryset, view):
        try:
            method = request.method
        except Exception:
            raise Exception('Something wrong happened')

        if method != 'GET':
            raise Exception('Method is not allowed!')

        try:
            search_terms = request.query_params
        except Exception:
            raise Exception(
                'Something wrong happened. Can not get a request.query_params')

        group_include = search_terms.getlist(self.group_arg_name)
        group_include_field = {
            name for name in group_include if name} & GROUP_ARG_NAME
        ordering_include = search_terms.getlist(self.ordering_arg_name)

        if not group_include_field:
            return queryset

        if len(group_include_field) == 1:

            return self.ordering__queryset(
                ordering_include, group_include_field)

        if len(group_include_field) == 2:
            for field in group_include_field:
                if field not in GROUP_ARG_NAME:
                    raise Exception(
                        'GROUP_BY is only available for GROUP_ARG_NAME'
                        'and shop fields!')

            return self.ordering__queryset(
                ordering_include, group_include_field)

        return queryset
