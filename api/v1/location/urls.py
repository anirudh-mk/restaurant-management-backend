from django.urls import path
from . import views

urlpatterns = [
    path('country/<str:pk>/', views.CountryAPI.as_view())
]