from rest_framework import serializers
from .models import ShopCard

class ShopCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopCard
        fields = "__all__"