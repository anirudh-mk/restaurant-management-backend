from django.urls import path

from . import views

urlpatterns = [
    path('restarurant/', views.RestaurantAPI.as_view(), name='restauarant_get_post_api'),
    path('restarurant/<str:pk>/', views.RestaurantAPI.as_view(), name='restauarant_edit_delete_api'),
    path('restarurant/get/<str:restaurant_id>/', views.RestaurantAPI.as_view(), name='restauarant_single_view_api'),
]
