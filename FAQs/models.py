from django.db import models

class FAQs(models.Model):
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.question}"
