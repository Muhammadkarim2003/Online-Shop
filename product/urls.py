from django.urls import path
from .views import ProductCreated, ProductList, ProductRetriev, ProductUpdate, ProductDelete, CalculateTotalPrice, ExpiredProducts



urlpatterns = [
    path('product_created/', ProductCreated.as_view()),
    path('product_list/', ProductList.as_view()),
    path('product_retriev/<uuid:pk>/', ProductRetriev.as_view()),
    path('product_update/<uuid:id>/', ProductUpdate.as_view()),
    path('product_delete/<uuid:pk>/', ProductDelete.as_view()),
    path('sum_total_products/', CalculateTotalPrice.as_view()),
    path('expire_product/', ExpiredProducts.as_view()),
]

