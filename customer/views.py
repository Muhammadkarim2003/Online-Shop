from django.shortcuts import render
from .models import Customer
from .serializers import CustomerSerializer
from rest_framework.response import Response
from rest_framework import status, views


#CUSTOMER MODELI UCHUN 
class CustomerCreated(views.APIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    def post(self, request, *args, **kvargs):
        data = request.data
        serializer = CustomerSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class CustomRetriev(views.APIView):
    def get(self, request, pk, *args, **kvargs):
        try:
            instance = Customer.objects.get(id=pk) 
            serializer = CustomerSerializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Customer.DoesNotExist:
            return Response({"detail": "Obyekt topilmadi !!!"}, status=status.HTTP_404_NOT_FOUND)
        
class CustomerList(views.APIView):
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CustomUpdate(views.APIView):
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
    def delete(self, request, pk, *args, **kwargs):
        try:
            instance = Customer.objects.get(id=pk)
            instance.delete()
            return Response({"detail": "Muvafaqiyatli o'chirildi !!!"}, status=status.HTTP_200_OK)
        except Customer.DoesNotExist:
            return Response({"detail": "Obyekt topilmadi !!!"}, status=status.HTTP_404_NOT_FOUND)

# class CustomPartialUpdate(views.APIView):
#     def patch(self, request, pk, *args, **kwargs):
#         try:
#             data = request.data
#             instance = Customer.objects.get(id=pk)
#             serializer = CustomerSerializer(instance, data=data, partial=True)
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except Customer.DoesNotExist:
#             return Response({"detail": "Obyekt topilmadi !!!"}, status=status.HTTP_404_NOT_FOUND)


