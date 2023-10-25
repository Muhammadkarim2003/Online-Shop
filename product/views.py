from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status, views
from datetime import datetime
from drf_yasg.utils import swagger_auto_schema


#PRODUCT MODELI UCHUN
class ProductCreated(views.APIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    @swagger_auto_schema(
        request_body=ProductSerializer,  
        responses={201: "Yaratildi"},
    )
    def post(self, request, *args, **kvargs):
        data = request.data
        serializer = ProductSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class ProductRetriev(views.APIView):
    @swagger_auto_schema(
        operation_description="""Bu yerda Productlarni idsi orqali olish mumkin""",
        operation_summary=""
    )
    def get(self, request, pk, *args, **kvargs):
        try:
            instance = Product.objects.get(id=pk)
            serializer = ProductSerializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({"detail": "Obyekt topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        

class ProductList(views.APIView):
    @swagger_auto_schema(
        operation_description="""Bu yerda barcha Productlarni olish mumkin""",
        operation_summary=""
    )
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ProductUpdate(views.APIView):
    @swagger_auto_schema(
        operation_description="""Bu yerda Productlarni idsi orqali yangilash mumkin""",
        operation_summary="",
        request_body=ProductSerializer
    )
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
    @swagger_auto_schema(
        operation_description="""Bu yerda Productlarni idsi orqali o'chirish mumkin""",
        operation_summary=""
    )
    def delete(self, request, pk, *args, **kvargs):
        try:
            instance = Product.objects.get(id=pk)
            instance.delete()
            return Response({"detail": "Muvafaqiyatli o'chirildi"}, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({"detail": "Obyekt topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        


class CalculateTotalPrice(views.APIView):
    @swagger_auto_schema(
        operation_description="""Marketdagi umumiy maxsulot summasini olish mumkin""",
        operation_summary=""
    )
    def get(self, request):
        products = Product.objects.all()
        if not products:
            return Response({'message': "Kechirasiz. Hozirda do'konda mahsulot yo'q"}, status=status.HTTP_404_NOT_FOUND)
        total_price = sum(product.price for product in products)
        
        return Response({'total_price': total_price}, status=status.HTTP_200_OK)
    


class ExpiredProducts(views.APIView):
    @swagger_auto_schema(
        operation_description="""Muddati o'tkan mahsulotlar""",
        operation_summary=""
    )
    def get(self, request):
        try:
            current_time = datetime.now()
            expired_products = Product.objects.filter(end_date__lt=current_time)
            data = [
                {
                    'name': product.name,
                    'end_date': product.end_date,
                }
                for product in expired_products
            ]
            return Response(data)
        except Product.DoesNotExist:
            return Response("Muddati o'tkan tovarlar topilmadi", status=status.HTTP_404_NOT_FOUND)