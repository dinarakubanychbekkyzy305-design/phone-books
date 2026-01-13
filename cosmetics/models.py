from django.db import models

class Cosmetic(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='cosmetic/', blank=True, null=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
