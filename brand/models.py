from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=40)
    image = models.CharField(max_length=400)

    def __str__(self):
        return f"{self.name}"