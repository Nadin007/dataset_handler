class RequestFieldsMixin(object):
    include_arg_name = 'show'
    exclude_arg_name = 'show!'
    MUST_GROUP_FIELDS = {'visitors', 'earnings'}
    MAY_GROUP_FIELDS = {'shop', 'country'}

    def __init__(self, *args, **kwargs) -> None:
        super(RequestFieldsMixin, self).__init__(*args, **kwargs)
        try:
            request = self.context['request']
            method = request.method
        except Exception:
            return

        if method != 'GET':
            return

        try:
            query_params = request.query_params
        except Exception:
            return

        include = query_params.getlist(self.include_arg_name)
        include_field = {name for name in include if name}

        exclude = query_params.getlist(self.exclude_arg_name)
        exclude_field = {name for name in exclude if name}

        group_fields = {name for name in query_params.getlist('group') if name}
        include_group_fields = group_fields & self.MAY_GROUP_FIELDS

        serializer_fields = set(self.fields)

        if (len(include_group_fields) > 0):
            include_group_fields |= self.MUST_GROUP_FIELDS
            exclude_field |= serializer_fields - include_group_fields

        fields_to_skip = serializer_fields & exclude_field
        if include_field:
            fields_to_skip |= serializer_fields - include_field

        for field in fields_to_skip:
            self.fields.pop(field)
