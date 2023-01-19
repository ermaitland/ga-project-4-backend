from django.db import models

class Requests(models.Model):
    products = models.ForeignKey('products.Products', related_name="requests", on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    user = models.ForeignKey('jwt_auth.User', related_name="requests", on_delete=models.CASCADE)