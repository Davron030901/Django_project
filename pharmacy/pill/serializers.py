from rest_framework import serializers
from .models import PILL

class PillSerializer(serializers.ModelSerializer):
    class Meta:
        model = PILL
        fields = '__all__'