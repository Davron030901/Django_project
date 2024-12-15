from django.db import models

# Create your models here.
class Profile(models.Model):
    BG_CHOICES=(
        ('red','Red'),
        ('blue','Blue'),
        ('green','Green')
        )
    name=models.CharField(max_length=300)
    slug=models.SlugField(max_length=100)
    bg_clor=models.CharField(max_length=100,choices=BG_CHOICES)
    
    def __str__(self):
        return self.name
    
class Link(models.Model):
    text=models.CharField(max_length=300)
    url=models.URLField(max_length=300)
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='links')
    
    def __str__(self):
        return f"{self.text} | {self.url}"