from rest_framework.views import APIView
from db.models import Country, State, District
from rest_framework.response import Response
from .serializer import CountrySerializer, StateSerializer, DistrictSerializer


class CountryAPI(APIView):
    def get(self, request):
        country_instance = Country.objects.all()
        serializer = CountrySerializer(country_instance, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Country created successfully")
        return Response(serializer.errors)

    def patch(self, request, pk):
        country_instance = Country.objects.filter(pk=pk).first()
        if not country_instance:
            return Response("Country not found")
        serializer = CountrySerializer(country_instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Country edited successfully")
        return Response(serializer.errors())

    def delete(self, request, pk):
        if country_instance := Country.objects.filter(pk=pk).first():
            country_instance.delete()
            return Response("Country deleted successfully")
        return Response("Country not found")


class StateAPI(APIView):
    def get(self, request):
        country_id = request.GET.get('country_id')
        state_instance = State.objects.filter(country=country_id)
        serializer = StateSerializer(state_instance, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("State created successfully")
        return Response(serializer.errors)

    def patch(self, request, pk):
        state_instance = State.objects.filter(pk=pk).first()
        if not state_instance:
            return Response("State not found")
        serializer = StateSerializer(state_instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Country edited successfully")
        return Response(serializer.errors())

    def delete(self, request, pk):
        if state_instance := State.objects.filter(pk=pk).first():
            state_instance.delete()
            return Response("State deleted successfully")
        return Response("State not found")


class DistrictAPI(APIView):
    def get(self, request):
        state_id = request.GET.get('state_id')
        district_instance = District.objects.filter(state=state_id)
        serializer = DistrictSerializer(district_instance, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DistrictSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("District created successfully")
        return Response(serializer.errors)

    def patch(self, request, pk):
        district_instance = District.objects.filter(pk=pk).first()
        if not district_instance:
            return Response("District not found")
        serializer = DistrictSerializer(district_instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("District edited successfully")
        return Response(serializer.errors())

    def delete(self, request, pk):
        if district_instance := District.objects.filter(pk=pk).first():
            district_instance.delete()
            return Response("District deleted successfully")
        return Response("District not found")
