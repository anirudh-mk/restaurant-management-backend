from django.urls import path
from . import views

urlpatterns = [
    path('country/', views.CountryAPI.as_view(), name='country_get_post_api'),
    path('country/<str:pk>/', views.CountryAPI.as_view(), name='country_patch_delete_api'),
    path('state/', views.StateAPI.as_view(), name='state_get_post_api'),
    path('state/<str:pk>/', views.StateAPI.as_view(), name='state_patch_delete_api'),
]