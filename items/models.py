from django.db import models
import uuid
from product.models import Product
from shopcard.models import ShopCard

# Create your models here.
class Items(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, null=False, primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    shopcard = models.ForeignKey(ShopCard, on_delete=models.CASCADE)
    sell_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.product)