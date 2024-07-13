

# Create your models here.
# myapp/models.py
from django.db import models

class City(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    countrycode = models.CharField(max_length=3)
    district = models.CharField(max_length=255)
    population = models.IntegerField()

    class Meta:
        managed = False  # No migrations will be created
        db_table = 'city'
