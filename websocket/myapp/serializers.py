


from .models import Category
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    class Meta:
        model = Product
        fields = '__all__'

        