from django.db import models
from django.contrib.auth.models import User

# # model for user information
# class Profile(models.Model):
#   user = models.OneToOneField(User, on_delete = models.CASCADE)
#   photo = models.ImageField(blank=True, upload_to='profile')
#   # name = models.CharField(max_length = 50)

#   def __str__(self):
#     return f"profile of {self.user.username}"
  
# # login information of user
# class Log(models.Model):
#   profile = models.ForeignKey(Profile, on_delete=models.CASCADE,
#                               blank=True, null=True)
#   photo = models.ImageField(upload_to='login')
#   is_correct = models.BooleanField(default=False)

#   def __str__ (self):
#     return str(self.id)
