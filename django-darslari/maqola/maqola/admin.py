from django.contrib import admin
from maqola.models import Maqola

@admin.register(Maqola)
class MaqolaAdmin(admin.ModelAdmin):
    list_display = ('id','title','author','created')
    class Meta:
        model = Maqola
