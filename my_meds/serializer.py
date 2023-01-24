from rest_framework import serializers
from products.serializer.common import ProductSerializer
from .models import MyMeds

class MyMedsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyMeds
        fields = '__all__'

class PopulatedMedsSerializer(MyMedsSerializer):
    products = ProductSerializer(many=True)