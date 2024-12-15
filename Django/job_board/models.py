from django.db import models

# Create your models here.
class JobPosting(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    company = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.title} ({self.company}) | Active: {self.is_active}"