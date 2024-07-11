'''models for product and category'''

from django.db import models


# Create your models here.
class ExhibitsCategories(models.Model):
    '''model for category'''
    name = models.CharField(max_length=64)
    descriptions = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Exhibits(models.Model):
    '''model for product'''

    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to='product_image', blank=True)
    descriptions = models.TextField(blank=True, null=True)
    category = models.ForeignKey(ExhibitsCategories, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} | {self.category}'
