from django.urls import path

from . import views

urlpatterns = [
    path('restarurant/', views.RestaurantAPI.as_view(), name='restauarant_get_post_api'),
    path('restarurant/<str:restaurant_id>/', views.RestaurantAPI.as_view(), name='restauarant_single_view_api'),
]
