from django.urls import path

from . import views

urlpatterns = [
    path('category/', views.CategoryAPI.as_view(), name='catogery_get_post_api'),
    path('category/<str:resturent_id>', views.CategoryAPI.as_view(), name='catogery_get_api'),
    path('category/<str:pk>', views.CategoryAPI.as_view(), name='catogery_edit_delete_api'),
]