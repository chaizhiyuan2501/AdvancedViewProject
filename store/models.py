from django.db import models

# Create your models here.
class Items(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()

    class Mete:
        db_table ="items"