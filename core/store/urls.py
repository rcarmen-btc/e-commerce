from django.urls import path, include

from .views import ProductList, ProductDetail, ProductCreate

app_name = 'store'

urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('create/', ProductCreate.as_view(), name='product_create'),
    path('category/<slug:slug>', ProductList.as_view(), name='product_category_list'),
    path('<slug:slug>', ProductDetail.as_view(), name='product_detail'),
]
