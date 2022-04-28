from rest_framework import serializers
from . models import warehouse_stocks

class stockSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = warehouse_stocks
        fields = ('Mfd_id', 'Name', 'UnitPrice', 'UnitsInStock')