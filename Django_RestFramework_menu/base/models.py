from django.db import models


class Item(models.Model):
    name=models.CharField(max_length=250)
    price=models.IntegerField()
    created=models.DateTimeField(auto_now_add=True)