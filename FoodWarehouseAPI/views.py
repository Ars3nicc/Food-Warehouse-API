from django.shortcuts import render
from rest_framework import viewsets
from . serializers import stockSerializers
from . models import warehouse_stocks

class stockViewSet(viewsets.ModelViewSet):
    queryset = warehouse_stocks.objects.all().order_by('Name')
    serializer_class = stockSerializers
