from django.shortcuts import render
from rest_framework import generics
from .models import Item
from .serializer import ItemSerializer
# Create your views here.
class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
