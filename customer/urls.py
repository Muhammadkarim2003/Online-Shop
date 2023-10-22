from django.urls import path
from .views import CustomerCreated, CustomRetriev, CustomerList, CustomUpdate, CustomDelete

urlpatterns = [
    path('customer_created/', CustomerCreated.as_view()),
    path('customer_retriev/<uuid:pk>/', CustomRetriev.as_view()),
    path('customer_list/', CustomerList.as_view()),
    path('customer_update/<uuid:pk>/', CustomUpdate.as_view()),
    path('customer_delete/<uuid:pk>/', CustomDelete.as_view()),
]
