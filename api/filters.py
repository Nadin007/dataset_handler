from django.db.models import Sum
from rest_framework import filters

from db_handler.models import ShopsDB


class DateFilter(filters.SearchFilter):

    def filter_queryset(self, request, queryset, view):
        try:
            method = request.method
            search_terms = request.GET
        except Exception:
            return
        if method != 'GET':
            return

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


class GroupFilterMixin(object):

    group_arg_name = 'group'
    ordering_arg_name = 'o'

    def ordering__queryset(
       self, queryset, ordering_include, group_include_field):

        ordering_include_field = {name for name in ordering_include if name}

        order_name = (
                '-earnings' if '-earnings' in ordering_include_field
                else 'earnings')
        try:
            if group_include_field == 2:
                order_name = (
                    '-visitors' if '-visitors' in ordering_include_field
                    else 'visitors')

                return ShopsDB.objects.values('country', 'shop').annotate(
                    visitors=Sum('visitors')).order_by(order_name)

            return ShopsDB.objects.values('country').annotate(
                earnings=Sum('earnings')).order_by(order_name)

        except Exception as s:
            raise Exception('Something wrong happened') from s

    def filter_queryset(self, request, queryset, view):
        try:
            method = request.method
        except Exception:
            return Exception('Something wrong happened')

        if method != 'GET':
            return Exception('Method isn alloved!')

        try:
            search_terms = request.query_params
        except Exception:
            return Exception(
                'Something wrong happened. Can not get a request.query_params')

        group_include = search_terms.getlist(self.group_arg_name)
        group_include_field = {name for name in group_include if name}
        ordering_include = search_terms.getlist(self.ordering_arg_name)

        if not group_include_field:
            return queryset

        if len(group_include_field) == 1:
            if 'country' not in group_include_field:
                return queryset

            self.ordering__queryset(
                queryset, ordering_include, group_include_field)

        if len(group_include_field) == 2:
            if ('country' and 'shop') not in group_include_field:
                raise Exception(
                    'GROUP_BY is only available for country and shop fields!')

            self.ordering__queryset(
                queryset, ordering_include, group_include_field)

        return queryset
