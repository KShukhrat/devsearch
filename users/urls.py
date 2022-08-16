from django.urls import path
from .views import *

urlpatterns = [
    path('logout', logoutUser, name='logout'),
    path('login/', loginUser, name='login'),
    # path('register/', registerUser, name='register'),


    path('', profiles, name='profiles'),
    path('profile/<str:pk>/', userProfile, name='user-profile'),
]