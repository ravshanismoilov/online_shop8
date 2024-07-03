from django.db import models
from django.core.validators import  MinValueValidator, MaxValueValidator


class Category(models.Model):
    name = models.CharField(max_length=155)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'


class Products(models.Model):
    category = models.ForeignKey(to=Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=155)
    year = models.DateField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='img/', blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return f'{self.category} {self.name}'

    class Meta:
        db_table = 'products'


class Review(models.Model):
    body = models.TextField()
    star_given = models.IntegerField(default=1, validators=[
        MaxValueValidator(5),
        MinValueValidator(0)
    ])
    product = models.ForeignKey(to=Products, on_delete=models.SET_NULL, null=True)
    user = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.product} {self.user} {self.star_given}'

    class Meta:
        db_table = 'review'

