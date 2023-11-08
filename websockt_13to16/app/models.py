from django.db import models

# Create your models here.

#  table for chat 
class Chat(models.Model):
    content = models.CharField(max_length=1000)
    timmestamp = models.DateTimeField(auto_now=True)
    group = models.ForeignKey('Group', on_delete=models.CASCADE)

# table for Group 
class Group(models.Model):
    name = models.CharField(max_length=255)   

    def __str__(self):
        return self.name
