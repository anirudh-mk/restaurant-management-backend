from rest_framework.response import Response
from rest_framework.views import APIView

from api.v1.food.serializer import CategorySerializer
from db.models import Food, Category


class CategoryAPI(APIView):
    def get(self, request, resturent_id=None):
        if resturent_id:
            category_instance = Category.objects.filter(
                food_category_query__restaurant__id=resturent_id
            )
            serializer = CategorySerializer(category_instance, many=True)
            return Response(serializer.data)

        category_instance = Category.objects.all()
        serializer = CategorySerializer(category_instance, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Category created successfully")
        return Response(serializer.errors)

    def patch(self, request, pk):
        country_instance = Category.objects.filter(pk=pk).first()
        if not country_instance:
            return Response("Category not found")
        serializer = CategorySerializer(country_instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Category edited successfully")
        return Response(serializer.errors())

    def delete(self, request, pk):
        if category_instance := Category.objects.filter(pk=pk).first():
            category_instance.delete()
            return Response("Category deleted successfully")
        return Response("Category not found")
