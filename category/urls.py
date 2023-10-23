from django.urls import path
from .views import CategoryCreated, CategoryList, CategoryRetriev, CategoryUpdate, categoryDelete, MostSoldProductsAPIView


urlpatterns = [
    path('category_created/', CategoryCreated.as_view()),
    path('category_list/', CategoryList.as_view()),
    path('category_retriev/<uuid:pk>/', CategoryRetriev.as_view()),
    path('category_update/<uuid:pk>/', CategoryUpdate.as_view()),   
    path('category_delete/<uuid:pk>/', categoryDelete.as_view()),
    path('sold_products/', MostSoldProductsAPIView.as_view()),
]