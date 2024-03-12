from rest_framework import serializers
from Core.models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= Products
        fields= '__all__'