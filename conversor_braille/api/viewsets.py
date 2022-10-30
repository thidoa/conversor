from rest_framework import viewsets
from conversor_braille.api import serializers
from conversor_braille import models


class AlfabetoViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.AlfabetoSerializer
    queryset = models.Alfabeto.objects.all()   