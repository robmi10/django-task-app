from django.db.models import fields
from rest_framework import serializers
from .models import Task, Taskitem, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','User', 'Password')

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id','author', 'title', 'description', 'responsibility', 'completed', 'created_at')

class TaskItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taskitem
        fields = ('id', 'author', 'title', 'description', 'responsibility', 'completed' ,'created_at')