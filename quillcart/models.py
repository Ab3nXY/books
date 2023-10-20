from django.db import models

class Book(models.Model):
    custom_id = models.DecimalField(max_digits=13, decimal_places=0, primary_key=True)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, null=True, blank=True)
    authors = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    published_date = models.DateField()
    category = models.CharField(max_length=255)
    distribution_expense = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title
