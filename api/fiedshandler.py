class RequestFieldsMixin(object):
    include_arg_name = 'show'
    exclude_arg_name = 'show!'

    def __init__(self, *args, **kwargs) -> None:
        super(RequestFieldsMixin, self).__init__(*args, **kwargs)
        try:
            request = self.context['request']
            method = request.method
        except Exception as s:
            return f'Error: {s}'

        if method != 'GET':
            return

        try:
            query_params = request.query_params
        except Exception as s:
            return f'Error: {s}'

        include = query_params.getlist(self.include_arg_name)
        include_field = {name for name in include if name}

        exclude = query_params.getlist(self.exclude_arg_name)
        exclude_field = {name for name in exclude if name}
        if not include_field and not exclude_field:
            return
        serializer_fields = set(self.fields)

        fields_to_skip = serializer_fields & exclude_field
        if include_field:
            fields_to_skip |= serializer_fields - include_field

        for field in fields_to_skip:
            self.fields.pop(field)
