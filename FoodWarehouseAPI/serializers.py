from rest_framework import serializers
from . models import warehouse_stock

class stockSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = warehouse_stock
        fields = ('Mfd_id', 'Name', 'UnitPrice', 'UnitsInStock')