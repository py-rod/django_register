from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    create = models.DateTimeField(auto_now_add=True)
    datecomplete = models.DateField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"Title: {self.title} || User: {self.user}"