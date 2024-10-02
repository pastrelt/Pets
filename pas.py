from django.db import models


class User(models.Model):
    email = models.CharField(max_length=255)
    token = models.CharField(max_length=2, choices=POSITIONS, default=cashier)


class Breed(models.Model):
    breed = models.CharField(max_length=255)


class ListPets(models.Model):
    color = models.DateTimeField(auto_now_add=True)
    age = models.FloatField(default=0.0)
    pickup = models.BooleanField(default=False)
    description = models.BooleanField(default=False)
    user = models.ForeignKey(Product, on_delete=models.CASCADE)
    breed = models.ForeignKey(Product, on_delete=models.CASCADE)