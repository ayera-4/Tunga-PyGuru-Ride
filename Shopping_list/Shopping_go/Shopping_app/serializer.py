from .models import *
from rest_framework.serializers import ModelSerializer, SerializerMethodField, ImageField, ReadOnlyField
class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'