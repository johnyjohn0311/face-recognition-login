# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from profiles.models import Profile

# thông tin người dùng đăng nhập
class Log(models.Model):
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE,
                              blank=True, null=True)
  photo = models.ImageField(blank=True, upload_to='login')
  is_correct = models.BooleanField(default=False)

  def __str__ (self):
    return str(self.id)
