from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status, views

#PRODUCT MODELI UCHUN
class ProductCreated(views.APIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def post(self, request, *args, **kvargs):
        data = request.data
        serializer = ProductSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class ProductRetriev(views.APIView):
    def get(self, request, pk, *args, **kvargs):
        try:
            instance = Product.objects.get(id=pk)
            serializer = ProductSerializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({"detail": "Obyekt topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        

class ProductList(views.APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ProductUpdate(views.APIView):
    def put(self, request, pk, *args, **kvargs):
        try:
            data = request.data
            instance = Product.objects.get(id=pk)
            serializer = ProductSerializer(data=data, instance=instance)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({'detail': "Obyekt topilmadi !!!"}, status=status.HTTP_404_NOT_FOUND)
class ProductDelete(views.APIView):
    def delete(self, request, pk, *args, **kvargs):
        try:
            instance = Product.objects.get(id=pk)
            instance.delete()
            return Response({"detail": "Muvafaqiyatli o'chirildi"}, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({"detail": "Obyekt topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        
