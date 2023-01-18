from django.db import models

class Requests(models.Model):
    item_name = models.CharField(max_length=30)
    text = models.CharField(max_length=300)
