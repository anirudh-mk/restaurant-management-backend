from rest_framework.views import APIView
from db.models import Country, State, District

from utils.response import CustomResponse
from .serializer import CountrySerializer, StateSerializer, DistrictSerializer


class CountryAPI(APIView):
    def get(self, request):
        country_instance = Country.objects.all()
        serializer = CountrySerializer(country_instance, many=True)
        return CustomResponse(response=serializer.data).get_success_response()

    def post(self, request):
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return CustomResponse(general_message='Country created successfully').get_success_response()
        return CustomResponse(response=serializer.errors).get_failure_response()

    def patch(self, request, pk):
        country_instance = Country.objects.filter(pk=pk).first()
        if not country_instance:
            return CustomResponse(general_message='Country not found').get_failure_response()
        serializer = CountrySerializer(country_instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return CustomResponse(general_message='Country edited successfully').get_success_response()
        return CustomResponse(response=serializer.errors).get_failure_response()

    def delete(self, request, pk):
        if country_instance := Country.objects.filter(pk=pk).first():
            country_instance.delete()
            return CustomResponse(general_message='Country deleted successfully').get_success_response()
        return CustomResponse(general_message='Country not found').get_failure_response()


class StateAPI(APIView):
    def get(self, request, country_id=None):
        state_instance = State.objects.filter(country=country_id)
        serializer = StateSerializer(state_instance, many=True)
        return CustomResponse(response=serializer.data).get_success_response()

    def post(self, request):
        serializer = StateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return CustomResponse(general_message='State created successfully').get_success_response()
        return CustomResponse(response=serializer.errors).get_failure_response()

    def patch(self, request, pk):
        state_instance = State.objects.filter(pk=pk).first()
        if not state_instance:
            return CustomResponse(general_message='State not found').get_failure_response()
        serializer = StateSerializer(state_instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return CustomResponse(general_message='State edited successfully').get_success_response()
        return CustomResponse(response=serializer.errors).get_failure_response()

    def delete(self, request, pk):
        if state_instance := State.objects.filter(pk=pk).first():
            state_instance.delete()
            return CustomResponse(general_message='State deleted successfully').get_success_response()
        return CustomResponse(general_message='state not found').get_failure_response()


class DistrictAPI(APIView):
    def get(self, request, state_id=None):
        district_instance = District.objects.filter(state=state_id)
        serializer = DistrictSerializer(district_instance, many=True)
        return CustomResponse(response=serializer.data).get_success_response()

    def post(self, request):
        serializer = DistrictSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return CustomResponse(general_message='District created successfully').get_success_response()
        return CustomResponse(response=serializer.errors).get_failure_response()

    def patch(self, request, pk):
        district_instance = District.objects.filter(pk=pk).first()
        if not district_instance:
            return CustomResponse(general_message='District not found').get_failure_response()
        serializer = DistrictSerializer(district_instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return CustomResponse(general_message='District edited successfully').get_success_response()
        return CustomResponse(response=serializer.errors).get_failure_response()

    def delete(self, request, pk):
        if district_instance := District.objects.filter(pk=pk).first():
            district_instance.delete()
            return CustomResponse(general_message='District deleted successfully').get_success_response()
        return CustomResponse(general_message='District not found').get_failure_response()