from django.db import models

# Create your models here. database
class Coders(models.Model):
    coder_number = models.PositiveIntegerField()
    first_name = models.CharField(max_length=12)
    last_name = models.CharField(max_length=12)
    lc_id = models.CharField(max_length=50)
    rating = models.PositiveIntegerField()

def __str__(self):
    return f'{self.first_name} {self.last_name}'