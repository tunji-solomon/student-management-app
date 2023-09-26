from django.db import models
import uuid


class Myuid(models.Model):
    id = models.UUIDField(primary_key=True, default=str(uuid.uuid4().int)[:6], editable=False, unique=True)



class Student(models.Model):
    SCIENCE = 'Science'
    COMMERCIAL = 'Commercial'
    ART = 'Art'
    SELECT = ' '

    DEPARTMENT = [
        (SELECT, 'Select'),
        (SCIENCE, 'Science'),
        (COMMERCIAL, 'Commercial'),
        (ART, 'Art')

    ]
    student_number = models.UUIDField(primary_key=True, default=str(uuid.uuid4().int)[:6], editable=False, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    department = models.CharField(max_length=20, choices= DEPARTMENT, default=SCIENCE)
    parent = models.ForeignKey(Our_user, default=False,on_delete=models.CASCADE)