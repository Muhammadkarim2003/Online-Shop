from django.db import models
from customer.models import Customer
import uuid

# Create your models here.
PAYMENT_CHOICES = [
    ('carta', 'Carta orqali'),
    ('naqd', 'Naqd pul orqali'),
    ('kredit_karta', 'Kredit karta orqali'),
    ('bank', 'Bank orqali'),
    ('paypal', 'PayPal orqali'),
]
class ShopCard(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, null=False, primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=20, decimal_places=5)
    payment = models.CharField(max_length=30, choices=PAYMENT_CHOICES)

    def __str__(self):
        return f"Total Price: {self.total_price}, Owner: {self.owner}"