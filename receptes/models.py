from django.db import models
from django.db.models import Avg , Sum

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    name = models.CharField(max_length=255)
    calories = models.PositiveSmallIntegerField()
    def __str__(self):
        return f"{self.name}"

class Recepie(models.Model):
    name =  models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="receptes/images",blank=True,null=True)
    recepie_ingridient = models.ManyToManyField(Product, through='ingridient')
    category = models.ManyToManyField(Category)
    def average_rating(self) -> float:
        return Rating.objects.filter(recepie=self).aggregate(Avg("rating"))["rating__avg"] or 0
    def total_calories(self)-> float:
        total_calories = 0
        ingredients = Ingridient.objects.filter(recepie=self)
        for ingredient in ingredients:
            total_calories += ingredient.product.calories * ingredient.amount
        return total_calories
    def __str__(self):
        return f"{self.name}: {self.average_rating()}"


class Ingridient(models.Model):
    recepie = models.ForeignKey(Recepie, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveSmallIntegerField()
    class Measure(models.Choices):
        mL = 'ml'
        g = 'g'
        gab = 'gab'
    measure = models.CharField(max_length=3,choices=Measure.choices)
    def __str__(self):
        return f"{self.recepie.name} / {self.product.name} {self.amount}{self.measure}"


class Rating(models.Model):
    recepie = models.ForeignKey(Recepie, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.recepie.name}: {self.rating}"
