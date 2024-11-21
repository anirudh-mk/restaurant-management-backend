from rest_framework import serializers

from db.models import Category, Food


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'created_at',
        ]


class PopularFoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = [
            'id',
            'name',
            'image',
            'rating',
            'price',
            'isVeg',
        ]