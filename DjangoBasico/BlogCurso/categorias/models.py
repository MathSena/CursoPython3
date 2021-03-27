from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome_cat = models.CharField(max_length=50)
