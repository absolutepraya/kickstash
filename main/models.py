from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=15)
    description = models.TextField()
    stock = models.IntegerField(default=1)

    @property
    def is_available(self):
        return self.stock > 0
