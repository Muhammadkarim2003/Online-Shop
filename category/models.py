from django.db import models
import uuid

# Create your models here.
class Category(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, null=False, primary_key=True)
    name = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.name