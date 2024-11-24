import uuid

from django.db import transaction
from rest_framework import serializers

from db.models import Category, Food, FoodImage, FoodIngredientsLink


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'image',
            'created_at',
        ]


class PopularFoodsSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    ingredients = serializers.SerializerMethodField()

    class Meta:
        model = Food
        fields = [
            'id',
            'name',
            'images',
            'rating',
            'price',
            'is_veg',
            'ingredients'
        ]

    def get_images(self, instance):
        return instance.food_image_food.values_list('image', flat=True)

    def get_ingredients(self, instance):
        return instance.food_ingredients_link_food.values_list('ingredient__name', flat=True)


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
        try:
            with transaction.atomic():
                validated_data['id'] = uuid.uuid4()
                food_instance = Food.objects.create(**validated_data)
                request = self.context.get('request')
                images = request.FILES.getlist('image')
                ingredients = request.data.get('ingredients', [])

                if not isinstance(ingredients, list):
                    ingredients = ingredients.split(',')

                FoodImage.objects.bulk_create([FoodImage(
                    id=uuid.uuid4(),
                    image=image,
                    food=food_instance,
                ) for image in images])

                FoodIngredientsLink.objects.bulk_create([
                    FoodIngredientsLink(
                        id=uuid.uuid4(),
                        ingredient_id=ingredient,
                        food=food_instance,
                    ) for ingredient in ingredients
                ])
        except Exception as e:
            raise serializers.ValidationError(str(e))
        return food_instance

    def validate_name(self, name):
        restaurant_id = self.initial_data.get('restaurant')
        if Food.objects.filter(name=name, restaurant=restaurant_id).exists():
            raise serializers.ValidationError('Food already exists')
        return name
