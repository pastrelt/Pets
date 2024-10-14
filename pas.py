from django.db import models


class User(models.Model):
    email = models.EmailField()
    token = models.CharField(max_length=60)


class Breed(models.Model):
    breed = models.CharField(max_length=80)


class ListPets(models.Model):
    color = models.CharField(max_length=80)
    age = models.IntegerField(default=0)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)