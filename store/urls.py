from django.urls import path, include

from .views import ProductList, ProductDetail, ProductCreate, add_good, UpdateProduct, DeleteProduct, SignUp

app_name = 'store'

urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('sign_up/', SignUp.as_view(), name='signup'),
    path('create_class/', ProductCreate.as_view(), name='product_create_class'),
    path('create/', add_good, name='product_create'),
    path('update_class/<slug:slug>', UpdateProduct.as_view(), name='product_update_class'),
    path('delete_class/<slug:slug>', DeleteProduct.as_view(), name='product_delete_class'),
    path('category/<slug:slug>', ProductList.as_view(), name='product_category_list'),
    path('<slug:slug>', ProductDetail.as_view(), name='product_detail'),
]
