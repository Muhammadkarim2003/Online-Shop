from django.shortcuts import render
from .models import Category
from .serializers import CategorySerializer
from rest_framework.response import Response
from rest_framework import views, status
from product.models import Product
from django.db.models import Count
from drf_yasg.utils import swagger_auto_schema




# CATEGORY MODELI UCHUN
class CategoryCreated(views.APIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    @swagger_auto_schema(
        request_body=CategorySerializer,  
        responses={201: "Yaratildi"},
    )
    def post(self, request, *args, **kvargs):
        data = request.data
        serializer = CategorySerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class CategoryRetriev(views.APIView):
    @swagger_auto_schema(
        operation_description="""Bu yerda categoriyaning id si orqali uni o'qish mumkin""",
        operation_summary=""
    )
    def get(self, request, pk, *args, **kvargs):
        try:
            instance = Category.objects.get(id=pk)
            serializer = CategorySerializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response({"detail": "Obyekt topilmadi !!!"}, status=status.HTTP_404_NOT_FOUND)


class CategoryList(views.APIView):
    @swagger_auto_schema(
        operation_description="""Bu yerda barcha categoriyalarni ko'rish mumkin""",
        operation_summary=""
    )
    def get(self, request):
        categorys = Category.objects.all()
        serializer = CategorySerializer(categorys, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryUpdate(views.APIView):
    @swagger_auto_schema(
        operation_description="""Bu yerda categoryani id si orqali yangilash mumkin""",
        operation_summary="",
        request_body=CategorySerializer
    )
    def put(self, request, pk, *args, **kvargs):
        try:
            data = request.data
            instance = Category.objects.get(id=pk)
            serializer = CategorySerializer(data=data, instance=instance)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response({"detail": "Obyekt topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        

class categoryDelete(views.APIView):
    @swagger_auto_schema(
        operation_description="""Bu yerda categoryani id si orqali o'chirish mumkin""",
        operation_summary=""
    )
    def delete(self, request, pk, *args, **kvargs):
        try:
            instance = Category.objects.get(id=pk)
            instance.delete()
            return Response({"detail": "Muvafaqiyatli o'chirildi"}, status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response({"detail": "Obyekt topilmadi"}, status=status.HTTP_404_NOT_FOUND)

class MostSoldProductsAPIView(views.APIView):
    @swagger_auto_schema(
        operation_description="""Bu yerda eng ko'p sotilgan mahsulotlarni ro'yhatini olish mumkin""",
        operation_summary=""
    )
    def get(self, request):
        categories = Category.objects.all()
        result = []

        for category in categories:
            most_sold_product = Product.objects.filter(category=category).annotate(
                sold_count=Count('items')
            ).order_by('-sold_count').first()

            if most_sold_product and most_sold_product.sold_count > 0:
                result.append({'category': category.name, 'product': most_sold_product.name, 'sold_count': most_sold_product.sold_count})

        return Response(result)

