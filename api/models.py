from django.db import models

class Transaction(models.Model):
    title = models.CharField(max_length=200)
    amount = models.FloatField()

    def __str__(self):
        return self.title
