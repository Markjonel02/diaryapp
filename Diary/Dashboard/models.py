from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.



class Entry(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    date_created = models.DateTimeField(default = timezone.now)
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title
class Profile(models.Model):
   about_me = models.TextField( null=True, blank=True)  
   image = models.ImageField(default ='hacker.gif', upload_to='profile_pics')
   user = models.OneToOneField(User, on_delete=models.CASCADE)

   def __str__(self):
      return self.user.username
       #null=True, blank=True