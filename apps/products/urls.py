from django.urls import path

from apps.products.views import ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view(), name="api_products"),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name="api_products_crud",)
]