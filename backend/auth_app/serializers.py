from rest_framework import serializers
from .models import CropProduct

class CropProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CropProduct
        fields = '__all__'
