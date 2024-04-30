from django.db import models

# Create your models here.

class enquiry(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    description=models.TextField(max_length=400)

    class Meta:
        db_table='enquiry'