from django.shortcuts import render
from .models import Customer
from .serializers import CustomerSerializer
from rest_framework.response import Response
from rest_framework import status, views
from drf_yasg.utils import swagger_auto_schema


#CUSTOMER MODELI UCHUN 
class CustomerCreated(views.APIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    @swagger_auto_schema(
        request_body=CustomerSerializer,
        operation_description="Bu yerda foydalanuvchi qo'shiladi",  
        responses={201: "Yaratildi"},
    )
    def post(self, request, *args, **kvargs):
        data = request.data
        serializer = CustomerSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class CustomRetriev(views.APIView):
    @swagger_auto_schema(
        operation_description="""Bu yerda foydalanuvchining id si orqali
          uning malumotlarini o'qish mumkin""",
        operation_summary=""
    )
    def get(self, request, pk, *args, **kvargs):
        try:
            instance = Customer.objects.get(id=pk) 
            serializer = CustomerSerializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Customer.DoesNotExist:
            return Response({"detail": "Obyekt topilmadi !!!"}, status=status.HTTP_404_NOT_FOUND)
        
class CustomerList(views.APIView):
    @swagger_auto_schema(
        operation_description="""Bu yerda barcha foydalanuvchilar (customer)
        chiqib keladi""",
        operation_summary=""
    )
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CustomUpdate(views.APIView):
    @swagger_auto_schema(
        operation_description="""Bu yerda foydalanuvchining id si orqali
          malumotlarini yangilash mumkin""",
        operation_summary="",
        request_body=CustomerSerializer
    )
    def put(self, request, pk, *args, **kvargs):
        try:
            data = request.data
            instance = Customer.objects.get(id=pk)
            serializer = CustomerSerializer(data=data, instance=instance)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Customer.DoesNotExist:
            return Response({"detail": "Obyekt topilmadi !!!"}, status=status.HTTP_404_NOT_FOUND)
    
        
class CustomDelete(views.APIView):
    @swagger_auto_schema(
        operation_description="""Bu yerda foydalanuvchining id si orqali
          uning malumotlarini o'chirib tashlash mumkin""",
        operation_summary=""
    )
    def delete(self, request, pk, *args, **kwargs):
        try:
            instance = Customer.objects.get(id=pk)
            instance.delete()
            return Response({"detail": "Muvafaqiyatli o'chirildi !!!"}, status=status.HTTP_200_OK)
        except Customer.DoesNotExist:
            return Response({"detail": "Obyekt topilmadi !!!"}, status=status.HTTP_404_NOT_FOUND)


