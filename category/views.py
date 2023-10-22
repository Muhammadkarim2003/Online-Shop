from django.shortcuts import render
from .models import Category
from .serializers import CategorySerializer
from rest_framework.response import Response
from rest_framework import views, status


# CATEGORY MODELI UCHUN
class CategoryCreated(views.APIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    def post(self, request, *args, **kvargs):
        data = request.data
        serializer = CategorySerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class CategoryRetriev(views.APIView):
    def get(self, request, pk, *args, **kvargs):
        try:
            instance = Category.objects.get(id=pk)
            serializer = CategorySerializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response({"detail": "Obyekt topilmadi !!!"}, status=status.HTTP_404_NOT_FOUND)


class CategoryList(views.APIView):
    def get(self, request):
        categorys = Category.objects.all()
        serializer = CategorySerializer(categorys, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryUpdate(views.APIView):
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
    def delete(self, request, pk, *args, **kvargs):
        try:
            instance = Category.objects.get(id=pk)
            instance.delete()
            return Response({"detail": "Muvafaqiyatli o'chirildi"}, status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response({"detail": "Obyekt topilmadi"}, status=status.HTTP_404_NOT_FOUND)

