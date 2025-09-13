from django.urls import path, include
from . import views
urlpatterns = [
    path("users", views.UserListCreateAPIView.as_view()),
    path("users/<str:username>", views.UserRetrieveUpdateDestroyView.as_view()),
]