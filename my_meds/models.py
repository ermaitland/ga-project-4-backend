from django.db import models

class MyMeds(models.Model):
    products = models.ManyToManyField('products.Products', related_name='my_meds')
    owner = models.ForeignKey('jwt_auth.User', related_name="my_meds", on_delete=models.CASCADE)

