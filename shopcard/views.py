from django.shortcuts import render
from .models import ShopCard
from .serializers import ShopCardSerializer
from rest_framework.response import Response
from rest_framework import status, views
from django.http import JsonResponse, HttpResponse
from django.db import models
import pandas as pd



# SHOPCGARD MODELU UCHUN
class ShopCardCreated(views.APIView):
    queryset = ShopCard.objects.all()
    serializer_class = ShopCardSerializer
    def post(self, request, *args, **kvargs):
        data = request.data
        serializer = ShopCardSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class ShopCardRetriev(views.APIView):
    def get(self, request, pk, *args, **kvargs):
        try:
            instance = ShopCard.objects.get(id=pk)
            serializer = ShopCardSerializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ShopCard.DoesNotExist:
            return Response({"detail": "Obyekt topilmadi !!!"}, status=status.HTTP_404_NOT_FOUND)
        
class ShopCardList(views.APIView):
    def get(self, request):
        shopcards = ShopCard.objects.all()
        serializer = ShopCardSerializer(shopcards, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ShopCardUpdate(views.APIView):
    def put(self, request, pk, *args, **kvargs):
        try:
            data = request.data
            instance = ShopCard.objects.get(id=pk)
            serializer = ShopCardSerializer(data=data, instance=instance)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ShopCard.DoesNotExist:
            return Response({"detail": "Obyekt topilmadi !!!"}, status=status.HTTP_404_NOT_FOUND)
        

class ShopCardDelete(views.APIView):
    def delete(self, request, pk, *args, **kvargs):
        try:
            instance = ShopCard.objects.get(id=pk)
            instance.delete()
            return Response({"detail": "Muvafaqiyatli o'chirildi"}, status=status.HTTP_200_OK)
        except ShopCard.DoesNotExist:
            return Response({"detail": "Obyekt topilmadi !!!"}, status=status.HTTP_404_NOT_FOUND)
        

def export_shopcard_history(request, pk):
    # ShopCard modelini chaqirish va serializer orqali ma'lumotlarni olish
    shopcards = ShopCard.objects.filter(owner__id=pk)
    serializer = ShopCardSerializer(shopcards, many=True)
    data = serializer.data

    # DataFrame yaratish
    df = pd.DataFrame(data)

    # Excel faylini yaratish
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = f'attachment; filename="shopcard_history.xlsx"'
    df.to_excel(response, index=False, engine='openpyxl')

    return response












# class ShopCardHistoryAPI(views.APIView):
#     def get(self, request, pk):
#         try:
#             shopcards = ShopCard.objects.filter(owner__id=pk)
#             serializer = ShopCardSerializer(shopcards, many=True)
#             return JsonResponse(serializer.data, safe=False)
#         except ShopCard.DoesNotExist:
#             return JsonResponse({'message': 'Foydalanuvchi uchun haridlar topilmadi.'}, status=status.HTTP_404_NOT_FOUND)
        

class CustomerPurchase(views.APIView):
    def get(self, request, pk):
        try:
            total_purchase = ShopCard.objects.filter(owner__id=pk).aggregate(total=models.Sum('total_price'))['total']
            if total_purchase and total_purchase > 1000000:
                return JsonResponse({"message": "Mijoz 1000000 so'mdan ko'p to'lov qilgan"}, status=status.HTTP_200_OK)
            else:
                return JsonResponse({"message": "Mijoz 1000000 so'mdan kam to'lov qilgan"}, status=status.HTTP_200_OK)
        except ShopCard.DoesNotExist:
            return JsonResponse({"message": "Foydalanuvchi uchun haridlar topilmadi."}, status=status.HTTP_404_NOT_FOUND)