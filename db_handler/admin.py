from django.contrib import admin

from .models import ShopsDB


class ShopsDBAdmin(admin.ModelAdmin):
    list_display = ('date', 'shop', 'country', 'visitors', 'earnings')
    search_fields = ('shop',)
    list_filter = ('date',)
    empty_value_display = '-пусто-'


admin.site.register(ShopsDB, ShopsDBAdmin)
