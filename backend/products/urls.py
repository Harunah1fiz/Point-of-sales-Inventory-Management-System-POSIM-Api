from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProductListCreateAPIView.as_view()),
    path("category/<str:category>", views.ProductByCategoryAPIView.as_view()),
    path("<str:lookup>", views.ProductRetrieveUpdateDestroy.as_view()),

]