from django.db import models

# Create your models here.
class Program(models.Model):
    code=models.CharField(max_length=10)
    description=models.TextField()
    duration=models.IntegerField()