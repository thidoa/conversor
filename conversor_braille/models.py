from unittest.util import _MAX_LENGTH
from django.db import models
from uuid import uuid4

# Create your models here.


class Alfabeto(models.Model):
    id_letra = models.CharField(max_length=255, primary_key=True, default=uuid4, editable=True)
    letra = models.CharField(max_length=1)
    idioma = models.CharField(max_length=100)
    letra_convertida = models.CharField(max_length=1)
