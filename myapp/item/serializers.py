from rest_framework import serializers
from .models import Ingredient, Item, Included

class IngredientsField(serializers.Field):
    def to_representation(self, value):
        return ','.join([ingredient.name for ingredient in value.all()])

class ProductsSerializer(serializers.ModelSerializer):
    imgUrl = serializers.SerializerMethodField('get_imgUrl')
    ingredients = IngredientsField()
    class Meta:
        model = Item
        fields = ('id', 'imgUrl', 'name', 'price', 'ingredients', 'monthlySales')
    def get_imgUrl(self, obj):
        return obj.full

class ProductDetailSerializer(serializers.ModelSerializer):
    imgUrl = serializers.SerializerMethodField('get_imgUrl')
    ingredients = IngredientsField()
    class Meta:
        model = Item
        fields = ('id', 'imgUrl', 'name', 'price', 'gender', 'category', 'ingredients', 'monthlySales')
    def get_imgUrl(self, obj):
        return obj.full

class RecommProductsSerializer(serializers.ModelSerializer):
    imgUrl = serializers.SerializerMethodField('get_imgUrl')
    class Meta:
        model = Item
        fields = ('id', 'imgUrl', 'name', 'price')
    def get_imgUrl(self, obj):
        return obj.thumb