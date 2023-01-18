from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=40)
    dose = models.CharField(max_length=10)
    brand = models.ForeignKey('brand.Brand', related_name="products", on_delete=models.CASCADE)
    category = models.CharField(max_length=3)
    image = models.CharField(max_length=400)
    form = models.CharField(max_length=75)
    interactions = models.CharField(max_length=300)
    side_effects = models.CharField(max_length=300)
    drive = models.BooleanField()
    food = models.BooleanField()
    primary_use = models.CharField(max_length=30)
    about = models.CharField(max_length=2000)
    owner = models.ForeignKey('jwt_auth.User', related_name="products", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
