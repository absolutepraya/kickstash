from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=15)
    description = models.TextField()

    @property
    def price_display(self):
        return f'Rp {self.price}'