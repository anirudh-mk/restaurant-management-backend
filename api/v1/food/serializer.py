import uuid

from rest_framework import serializers

from db.models import Category, Food, FoodImage


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
            'is_veg',
        ]


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = [
            'id',
            'name',
            'description',
            'price',
            'rating',
            'restaurant',
            'catogery',
            'is_veg',
            'created_at'
        ]

    def create(self, validated_data):
        validated_data['id'] = uuid.uuid4()
        food_instance = Food.objects.create(**validated_data)
        images = self.context.get('images')
        a = FoodImage.objects.bulk_create([FoodImage(
            id=uuid.uuid4(),
            image=image,
            food=food_instance,
        ) for image in images])
        return food_instance
