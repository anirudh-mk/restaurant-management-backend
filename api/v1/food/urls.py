from django.urls import path

from . import views

urlpatterns = [
    path('category/', views.CategoryAPI.as_view(), name='catogery_get_post_api'),
    path('category/list/<str:restaurant_id>/', views.CategoryAPI.as_view(), name='list_catogery_by_resturent_api'),
    path('category/<str:pk>/', views.CategoryAPI.as_view(), name='catogery_edit_delete_api'),
    path('popular/list/<str:restaurant_id>/', views.PopularFoodsAPI.as_view(), name='get_popular_foods_api'),
    path('', views.FoodAPI.as_view(), name='food_create_api'),
    path('<str:pk>/', views.FoodAPI.as_view(), name='food_edit_delete_api'),
    path('list/<str:restaurant_id>/', views.FoodAPI.as_view(), name='list_food_by_restaurant_api'),
    path('get/<str:food_id>/', views.FoodAPI.as_view(), name='food_details_api'),
]