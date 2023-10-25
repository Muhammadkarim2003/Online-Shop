from django.shortcuts import render
from .models import Items
from .serializers import ItemSerializer
from rest_framework.response import Response
from rest_framework import status, views
from drf_yasg.utils import swagger_auto_schema
from shopcard.models import ShopCard


#ITEMS MODELI UCHUN 


class ItemCreated(views.APIView):
    serializer_class = ItemSerializer

    @swagger_auto_schema(
        operation_description="""Bu yerda product va shopcard idsi orqali items yaratiladi""",
        request_body=ItemSerializer,
        responses={201: "Yaratildi"},
    )
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = ItemSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        shop_card = serializer.validated_data['shopcard']
        total_price = self.calculate_total_price(shop_card)
        shop_card.total_price = total_price
        shop_card.save()

        customer = shop_card.owner
        total_spent = self.calculate_customer_total_spent(customer)
        
        response_data = {
            "message": "Yaratildi",
            "customer": customer.id,
            "total_spent": total_spent,
        }
        
        return Response(response_data, status=status.HTTP_201_CREATED)

    def calculate_total_price(self, shop_card):
        items = Items.objects.filter(shopcard=shop_card)
        total_price = sum(item.product.price for item in items)
        return total_price
    
    def calculate_customer_total_spent(self, customer):
        shop_cards = ShopCard.objects.filter(owner=customer)
        total_spent = sum(shop_card.total_price for shop_card in shop_cards)
        return total_spent


    def calculate_total_price(self, shop_card):
        items = Items.objects.filter(shopcard=shop_card)
        total_price = sum(item.product.price for item in items)
        return total_price


class ItemRetriev(views.APIView):
    @swagger_auto_schema(
        operation_description="""Bu yerda itemlarni id si orqali ko'rish mumkin""",
        operation_summary=""
    )
    def get(self, request, pk, *args, **kvargs):
        try:
            instance = Items.objects.get(id=pk)
            serializer = ItemSerializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Items.DoesNotExist:
            return Response({"detail": "Obyekt topilmadi"}, status=status.HTTP_404_NOT_FOUND)

class ItemList(views.APIView):
    @swagger_auto_schema(
        operation_description="""Bu yerda barcha itemlarni ko'rish mumkin""",
        operation_summary=""
    )
    def get(self, request):
        items = Items.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ItemUpdate(views.APIView):
    @swagger_auto_schema(
        operation_description="""Bu yerda itemlarni idsi orqali yangilashingiz mumkin""",
        operation_summary="",
        request_body=ItemSerializer
    )
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
    @swagger_auto_schema(
        operation_description="""Bu yerda itemlarni idsi orqali o'chirish mumkin mumkin""",
        operation_summary=""
    )
    def delete(self, request, pk, *args, **kvargs):
        try:
            instance = Items.objects.get(id=pk)
            instance.delete()
            return Response({"detail": "Muvafaqiyatli o'chirildi !!!"}, status=status.HTTP_200_OK)
        except Items.DoesNotExist:
            return Response({"detail": "Obyekt topilmadi !!!"}, status=status.HTTP_404_NOT_FOUND)
        


