from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  password = models.CharField(max_length=150)
  
  
  def __str__(self) -> str:
    return self.user

    