from django.db import models


class modelA(models.Model):
    text = models.CharField(max_length=100)
    date = models.DateTimeField('data published')


class modelB(models.Model):
    modelA = models.ForeignKey(modelA, on_delete=models.CASCADE)
