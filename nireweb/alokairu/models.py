from django.db import models

class Pertsona(models.Model):
    name = models.CharField(max_length=255)

class Kotxea(models.Model):
    modeloa = models.CharField(max_length=255)
    data = models.CharField(max_length=255)
    pertsona = models.ForeignKey(Pertsona, on_delete=models.CASCADE, null=True)

