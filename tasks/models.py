from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(null=True)
    urgent = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self):  
        return self.title + ' - by ' + self.user.username
    
    