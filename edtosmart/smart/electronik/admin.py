from django.contrib import admin
from .models import Electronik

@admin.register(Electronik)
class TexnicAdmin(admin.ModelAdmin):
    list_display = ('id','name','category','image','color','model','count','created')
    class Meta:
        model = Electronik