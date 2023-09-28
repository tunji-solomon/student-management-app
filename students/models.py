
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



class Our_student(models.Model):

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

    student_number = models.PositiveIntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()
    department= models.CharField(max_length=50,choices=DEPARTMENT, default= SELECT)
    parent = models.ForeignKey(Our_user, default=False,on_delete=models.CASCADE)

    def __str__(self):

        return f'{self.first_name}  {self.last_name}'
    
class Testimonials(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=11)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.fullname

class Blog(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    brief = models.CharField(max_length=100,default=False)
    content = models.TextField()
    image = models.ImageField(upload_to='images')
    author = models.CharField(max_length=100, blank=True )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    class Meta:

        ordering = ['-created_on']

    def __str__(self):

        return self.title




    
    
    




