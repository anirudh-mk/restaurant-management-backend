from rest_framework.response import Response
from rest_framework.views import APIView

from api.v1.food.serializer import CategorySerializer
from db.models import Food, Category
from utils.response import CustomResponse


class CategoryAPI(APIView):
    def get(self, request, resturent_id=None):
        if resturent_id:
            category_instance = Category.objects.filter(
                food_category_query__restaurant__id=resturent_id
            ).distinct()

            serializer = CategorySerializer(category_instance, many=True)

            return CustomResponse(response=serializer.data).get_success_response()

        category_instance = Category.objects.all()
        serializer = CategorySerializer(category_instance, many=True)
        return CustomResponse(response=serializer.data).get_success_response()

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return CustomResponse(general_message="Category created successfully").get_success_response()
        return CustomResponse(response=serializer.errors).get_failure_response()

    def patch(self, request, pk):
        country_instance = Category.objects.filter(pk=pk).first()
        if not country_instance:
            return CustomResponse(general_message="Category not found").get_failure_response()
        serializer = CategorySerializer(country_instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return CustomResponse(general_message="Category edited successfully").get_success_response()
        return CustomResponse(response=serializer.errors).get_failure_response()

    def delete(self, request, pk):
        if category_instance := Category.objects.filter(pk=pk).first():
            category_instance.delete()
            return CustomResponse(general_message="Category deleted successfully").get_success_response()
        return CustomResponse(general_message="Category not found").get_failure_response()
