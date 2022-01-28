from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Person(models.Model):
    firstname = models.CharField(max_length=100)
    city = models.ManyToManyField(City)

    def __str__(self):
        return self.firstname
