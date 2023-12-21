from django.urls import path
from ..views.productview import *

urlpatterns=[
    path('products/<int:pk>/', ListProduct.as_view(), name='product-list'),
    path('product/<int:pk>/', DeleteProduct.as_view(), name='product-list-delete-update'),
    path('products/', ListAllProduct.as_view(), name='product-list-all'),
    path('products/search/<str:search>', ProductSearch.as_view(), name='product-search-all'),
    path('products/create/', CreateProduct.as_view(), name='product-list-create'),
]