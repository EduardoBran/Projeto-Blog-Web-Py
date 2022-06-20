from django.db import models


class Categoria(models.Model):
    nome_cat = models.CharField(max_length=50)
