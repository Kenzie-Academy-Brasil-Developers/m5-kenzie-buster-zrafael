from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
    path('users/', views.UserView.as_view()),
    path('users/login/', jwt_views.TokenObtainPairView.as_view()),
    path('users/<int:user_id>/', views.UserDetailView.as_view())
]