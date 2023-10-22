from django.urls import path
from .views import ItemCreated, ItemList, ItemRetriev, ItemUpdate, ItemDelete


urlpatterns = [
    path('item_created/', ItemCreated.as_view()),
    path('item_list/', ItemList.as_view()),
    path('item_retriev/<uuid:pk>/', ItemRetriev.as_view()),
    path('item_update/<uuid:pk>/', ItemUpdate.as_view()),
    path('item_delete/<uuid:pk>/', ItemDelete.as_view()),
]