from django.contrib import admin

from .models import Maqola
@admin.register(Maqola)
class MaqolaAdmin(admin.ModelAdmin):
    list_display=['id','title']
    class Meta:
        model=Maqola

