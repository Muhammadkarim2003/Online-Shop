from django.db import models
import uuid

# Create your models here.
class Customer(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, null=False, primary_key=True)
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=1000)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=13)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name