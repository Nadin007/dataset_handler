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
