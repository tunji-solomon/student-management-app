
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Our_user(models.Model):
    user = models.OneToOneField(User, blank=False,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    username = models.CharField(max_length=100,blank=False)
    email = models.EmailField(max_length=100, blank=False)
    password = models.CharField(max_length=100,blank=False)
    confirm_password = models.CharField(max_length=100, blank=False)
    phone = models.CharField(max_length=12, blank=False)

    def __str__(self):
        return self.user.username




class Student(models.Model):
    student_number = models.PositiveIntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    field_of_study = models.CharField(max_length=50)
    gpa = models.FloatField()
    parent = models.ForeignKey(Our_user, default=False,on_delete=models.CASCADE)
    
    




