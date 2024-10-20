from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
# Create your models here.
