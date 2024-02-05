from rest_framework import serializers, viewsets
from .models import CareerProfessional

class CareerProfessionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerProfessional
        fields = '__all__'

