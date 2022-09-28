from rest_framework import serializers
from product.models import Product


class ProductResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = serializers.ALL_FIELDS


class CreateProductSerializer(serializers.Serializer):
    name = serializers.CharField(
        max_length=255, required=True, trim_whitespace=True, min_length=3
    )
    price = serializers.IntegerField(required=True, min_value=1)
    description = serializers.CharField(
        required=True, trim_whitespace=True, min_length=1
    )
