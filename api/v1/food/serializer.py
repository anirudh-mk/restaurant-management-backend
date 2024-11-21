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
    images = serializers.SerializerMethodField()

    class Meta:
        model = Food
        fields = [
            'id',
            'name',
            'images',
            'rating',
            'price',
            'is_veg',
        ]

    def get_images(self, instance):
        return instance.food_image_food.values_list('image', flat=True)


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
        FoodImage.objects.bulk_create([FoodImage(
            id=uuid.uuid4(),
            image=image,
            food=food_instance,
        ) for image in images])
        return food_instance

    def validate_name(self, name):
        restaurant_id = self.initial_data.get('restaurant')
        if Food.objects.filter(name=name, restaurant=restaurant_id).exists():
            raise serializers.ValidationError('Food already exists')
        return name