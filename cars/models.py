from django.db import models
from django.contrib.auth import get_user_model

class Car(models.Model):
    name = models.CharField(max_length=64)
    maker = models.CharField(max_length=64)
    year = models.IntegerField()
    admin = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name
