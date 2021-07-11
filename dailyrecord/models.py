from django.db import models
# from enum import Enum

# class Category(Enum):
# 	entertainment = 1
#   eat = 2
#   sleep = 3
# 	learn = 4
# 	transport = 5
#   work = 6
  


class DailyRecord(models.Model):
  name = models.CharField(max_length=150)
  category = models.IntegerField()
  startime = models.DateTimeField(blank=True)
  endtime = models.DateTimeField(blank=True)


  def __str__(self) -> str:
    return self.name