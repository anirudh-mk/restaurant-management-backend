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

    def validate_name(self, name):
        country = self.initial_data.get('country')
        if State.objects.filter(name=name, country=country).exists():
            raise serializers.ValidationError('State already exists')
        return name


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = [
            'id',
            'name',
            'state',
            'created_at'
        ]

    def validated_name(self, name):
        state = self.initial_data.get('state')
        if State.objects.filter(name=name, state=state).exists():
            raise serializers.ValidationError('District already exists')
        return name
