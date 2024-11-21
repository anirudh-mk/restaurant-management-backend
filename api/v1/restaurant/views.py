from rest_framework.views import APIView

from api.v1.restaurant.serializer import RestaurantSerializer
from db.models import Restaurant
from utils.response import CustomResponse


class RestaurantAPI(APIView):
    def get(self, request, restaurant_id=None):
        if restaurant_id:
            restaurant_instance = Restaurant.objects.filter(id=restaurant_id).first()
            serializer = RestaurantSerializer(restaurant_instance, many=False)
            return CustomResponse(response=serializer.data).get_success_response()

        restaurant_instance = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurant_instance, many=True)
        return CustomResponse(response=serializer.data).get_success_response()

    def post(self, request):
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return CustomResponse(general_message='Restaurant created successfully').get_success_response()
        return CustomResponse(response=serializer.errors).get_failure_response()