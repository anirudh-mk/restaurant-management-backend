from rest_framework import serializers

from db.models import Country, State, District


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = [
            'id',
            'name',
            'created_at'
        ]


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = [
            'id',
            'name',
            'country',
            'created_at'
        ]


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = [
            'id',
            'name',
            'state',
            'created_at'
        ]
