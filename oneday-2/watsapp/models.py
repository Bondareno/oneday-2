from django.db import models
from django.utils import timezone


class Case(models.Model):
    name = models.CharField(max_length=70, default="")
    url = models.CharField(max_length=250)
    pattern = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Found(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    text = models.CharField(max_length=250)
    created = models.DateTimeField(default=timezone.now)


class News(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    oldtext = models.CharField(max_length=250)
    newtext = models.CharField(max_length=250)
    created = models.DateTimeField(default=timezone.now)
