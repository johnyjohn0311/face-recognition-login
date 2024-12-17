from django.db import models
from django.contrib.auth.models import User

# model for user information
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete = models.CASCADE, null=True)
  photo = models.ImageField(blank=True, upload_to='profile')

  def __str__(self):
    return f"profile of {self.user.username}"
  