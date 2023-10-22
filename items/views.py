from django.shortcuts import render
from .models import Items
from .serializers import ItemSerializer
from rest_framework.response import Response
from rest_framework import status, views

#ITEMS MODELI UCHUN 
class ItemCreated(views.APIView):
    queryset = Items.objects.all()
    serializer_class = ItemSerializer
    def post(self, request, *args, **kvargs):
        data = request.data
        serializer = ItemSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ItemRetriev(views.APIView):
    def get(self, request, pk, *args, **kvargs):
        try:
            instance = Items.objects.get(id=pk)
            serializer = ItemSerializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Items.DoesNotExist:
            return Response({"detail": "Obyekt topilmadi"}, status=status.HTTP_404_NOT_FOUND)

class ItemList(views.APIView):
    def get(self, request):
        items = Items.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ItemUpdate(views.APIView):
    def put(self, request, pk, *args, **kvargs):
        try:
            data = request.data
            instance = Items.objects.get(id=pk)
            serializer = ItemSerializer(data=data, instance=instance)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Items.DoesNotExist:
            return Response({"detail": "Obyekt topilmadi !!!"}, status=status.HTTP_404_NOT_FOUND)


class ItemDelete(views.APIView):
    def delete(self, request, pk, *args, **kvargs):
        try:
            instance = Items.objects.get(id=pk)
            instance.delete()
            return Response({"detail": "Muvafaqiyatli o'chirildi !!!"}, status=status.HTTP_200_OK)
        except Items.DoesNotExist:
            return Response({"detail": "Obyekt topilmadi !!!"}, status=status.HTTP_404_NOT_FOUND)
