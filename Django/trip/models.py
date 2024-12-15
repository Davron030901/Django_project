from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
User=get_user_model()
# Create your models here.
class Trip(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE,related_name='trips')
    
    
    def __str__(self):
        return self.city
    
    
class Note(models.Model):
    EXCURSION=(
        ('event',"Event"),
        ('place',"Place"),
        ('restaurant',"Restaurant"),
        ('other',"Other"),
    )
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE,related_name='notes')
    name=models.CharField(max_length=100)
    description=models.TextField()
    type=models.CharField(max_length=100,choices=EXCURSION)
    img=models.ImageField(upload_to='images/',null=True,blank=True)
    rating=models.PositiveSmallIntegerField(default=1,validators=[MaxValueValidator(5)])
    def __str__(self):
        return f"{self.name} | {self.trip.city}"