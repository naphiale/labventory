from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    # rating = models.IntegerField()

    def __str__(self):
        return self.name

    @property
    def is_highly_rated(self):
        return self.rating >= 4
