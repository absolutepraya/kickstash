from django.db import models
import uuid
from django.contrib.auth.models import User


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=0, max_digits=15)
    description = models.TextField()
    stock = models.IntegerField(default=1)

    @property
    def is_available(self):
        return self.stock > 0
