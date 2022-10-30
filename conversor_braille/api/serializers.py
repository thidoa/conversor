from rest_framework import serializers
from conversor_braille import models


class AlfabetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Alfabeto
        fields = '__all__'