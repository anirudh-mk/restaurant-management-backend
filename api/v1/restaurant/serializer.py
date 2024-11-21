import uuid

from rest_framework import serializers

from db.models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    district = serializers.CharField(source='district_id', write_only=True)
    district_name = serializers.CharField(source='district.name', read_only=True)
    state_name = serializers.CharField(source='district.state.name', read_only=True)
    country_name = serializers.CharField(source='district.state.country.name', read_only=True)

    class Meta:
        model = Restaurant
        fields = [
            'id',
            'name',
            'description',
            'address',
            'location',
            'district',
            'district_name',
            'state_name',
            'country_name',
            'created_at',
        ]

    def create(self, validated_data):
        validated_data['id'] = uuid.uuid4()
        return Restaurant.objects.create(**validated_data)