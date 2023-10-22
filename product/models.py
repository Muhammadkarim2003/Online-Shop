from django.db import models
from category.models import Category
import uuid

# Create your models here.
class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, null=False, primary_key=True)
    name = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=20, decimal_places=5)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name