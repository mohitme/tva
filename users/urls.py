from django.urls import path
from .views import *

urlpatterns = [
    path("users/", UserCreateListApi.as_view()),
    path("users/<int:pk>/", UserUpdateRetDelApi.as_view()),
]
