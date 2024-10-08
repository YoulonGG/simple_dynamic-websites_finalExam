from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name} ({self.id})"

class Product(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()  
    volume = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='Images/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.id})"
