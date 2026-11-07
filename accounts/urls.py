from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomLoginView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('complete-profile/', views.complete_profile, name='complete_profile'),
]