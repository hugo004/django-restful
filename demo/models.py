from django.db import models

# Create your models here.
class RecordModel(models.Model):
  id = models.AutoField(auto_created=True, primary_key=True)
  date = models.DateTimeField('date')
  members = models.IntegerField(max_length=10)
  district = models.CharField(max_length=100)
  location = models.CharField(max_length=100)
  restaurant = models.CharField(max_length=100)
  food_type = models.CharField(max_length=100)
  cost = models.DecimalField(max_digits=5, decimal_places=2)