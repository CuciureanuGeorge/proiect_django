from django.db import models


# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=200)
    population = models.IntegerField(default=0)

    def __str__(self):
        return self.name + " " + str(self.population)


class City(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default="")
    population = models.IntegerField(default=0)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.name + " " + self.description + " " + str(self.population)
