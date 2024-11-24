from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.RestaurantAPI.as_view(), name='restauarant_get_post_api'),
    path('<str:pk>/', views.RestaurantAPI.as_view(), name='restauarant_edit_delete_api'),
    path('get/<str:restaurant_id>/', views.RestaurantAPI.as_view(), name='restauarant_single_view_api'),
]
