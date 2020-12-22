from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField("Se tour",max_length=50)
    who_i = models.TextField("Yay kane")
    price = models.IntegerField()


    def __str__(self):
        return self.name
