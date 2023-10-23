from rest_framework import serializers
from .models import ShopCard

class ShopCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopCard
        fields = "__all__"
        total_price = serializers.DecimalField(max_digits=20, decimal_places=5)