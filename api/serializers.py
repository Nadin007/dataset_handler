from rest_framework import serializers

from db_handler.models import ShopsDB, User
from .fiedshandler import RequestFieldsMixin


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')
        ref_name = 'ReadOnlyUsers'


class ShopsDBSerializer(RequestFieldsMixin, serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed, contains function sorts
    API response data by group
    """
    class Meta:
        model = ShopsDB
        fields = ('date', 'shop', 'country', 'visitors', 'earnings')
        ref_name = 'ReadOnlyUsers'
