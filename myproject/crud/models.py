from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveBigIntegerField()

    def __str__(self):
        return self.name
