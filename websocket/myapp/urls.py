from django.urls import path
from . import views

urlpatterns = [
    # Category endpoints
    path("categories/", views.CategoryView.as_view()),  # GET, POST on /categories/
    path(
        "categories/<int:pk>/", views.CategoryView.as_view()
    ),  # GET, PUT, DELETE on /categories/<pk>/
    # Product endpoints
    path("products/", views.ProductView.as_view()),  # GET, POST on /products/
    path(
        "products/<int:pk>/", views.ProductView.as_view()
    ),  # GET, PUT, DELETE on /products/<pk>/
]
