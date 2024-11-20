from rest_framework.views import APIView
from db.models import Country
from rest_framework.response import Response
from .serializer import CountrySerializer


class CountryAPI(APIView):
    def get(self, request, pk=None):
        country_instance = Country.objects.all()
        serializer = CountrySerializer(country_instance, many=True)
        return Response(serializer.data)

    def post(self, request, pk=None):
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Country created successfully")
        return Response(serializer.errors)

    def patch(self, request, pk):
        if country_instance := Country.objects.filter(pk=pk).first():
            serializer = CountrySerializer(country_instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response("Country edited successfully")
            return Response(serializer.errors())
        return Response("Country not found")

    def delete(self, request, pk):
        if country_instance := Country.objects.filter(pk=pk).first():
            country_instance.delete()
            return Response("Country deleted successfully")
        return Response("Country not found")
