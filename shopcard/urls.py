from django.urls import path
from .views import (ShopCardCreated, ShopCardRetriev, ShopCardList, ShopCardUpdate,
                     ShopCardDelete, ShopCardHistoryAPI, CustomerPurchase)



urlpatterns = [
    path('shopcard_created/', ShopCardCreated.as_view()),
    path('shopcard_retriev/<uuid:pk>/', ShopCardRetriev.as_view()),
    path('shopcard_list/', ShopCardList.as_view()),
    path('shopcard_update/<uuid:pk>/', ShopCardUpdate.as_view()),
    path('shopcard_delete/<uuid:pk>/', ShopCardDelete.as_view()),
    path('shopcard_history/<uuid:pk>/', ShopCardHistoryAPI.as_view()),
    path('custom_pursache/<uuid:pk>/', CustomerPurchase.as_view()),
]
