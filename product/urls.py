from django.urls import path
from .views import HomePageView, CategoryView, ProductView, ProductDetail, CreateProduct


urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('category-view', CategoryView.as_view(), name='category-view'),
    path('category-detail/<int:pk>', ProductView.as_view(), name='category-detail'),
    path('product-detail/<int:pk>', ProductDetail.as_view(), name='product-detail'),
    path('create-product/', CreateProduct.as_view(), name='create-product'),
]