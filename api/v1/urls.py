from django.urls import path, include

urlpatterns = [
    path('user/', include('api.v1.user.urls')),
    path('location/', include('api.v1.location.urls')),
    path('food/', include('api.v1.food.urls')),
]