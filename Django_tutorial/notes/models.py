from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    title = models.CharField(max_length=100)  # Mavjud maydon
    text = models.TextField()  # Agar ishlatmoqchi bo'lsangiz, bu maydon kerak
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="notes")