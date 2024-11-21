from django.urls import path

from . import views

urlpatterns = [
    path('category/', views.CategoryAPI.as_view(), name='catogery_get_post_api'),
    path('category/get/<str:restaurant_id>/', views.CategoryAPI.as_view(), name='catogery_get_api'),
    path('category/<str:pk>/', views.CategoryAPI.as_view(), name='catogery_edit_delete_api'),
    path('popular/<str:restaurant_id>/', views.PopularFoodsAPI.as_view(), name='get_popular_foods_api'),
]