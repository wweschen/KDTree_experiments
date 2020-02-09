from django.db import models

# Create your models here.
class Demo_model (models.Model):
    text =  models.CharField(max_length=8000)