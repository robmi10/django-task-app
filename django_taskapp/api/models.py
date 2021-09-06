from django.db import models

class User(models.Model):
    User = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)

class Task(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    responsibility = models.CharField(max_length=100, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Taskitem(models.Model):
    task = models.ForeignKey(Task, null=True, on_delete=models.SET_NULL)
    author = models.CharField(max_length=100)
    taskitem = models.CharField(max_length=100, default="", unique=False)
    title = models.CharField(max_length=100)
    responsibility = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)