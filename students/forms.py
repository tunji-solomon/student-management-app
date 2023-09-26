from django import forms
from . models import *
from django.forms import *
from django.contrib.auth.models import User

class StudentForm(ModelForm):


   class Meta:
      
      model = Our_student
      fields = '__all__'
      widgets = {
         

         'student_number': NumberInput(attrs={
            'class': 'form-control',
            'style':'width:300px',
            'placeholder':'Enter student number'
         }),

         'first_name': TextInput(attrs={
            'class':'form-control',
            'style':'max-width: 300px',
            'placeholder':'Enter first name'
         }),

         
         'last_name': TextInput(attrs={
            'class':'form-control',
            'style':'max-width: 300px',
            'placeholder':'Enter first name'
         }),

         'dob': DateInput(attrs={
            'class':'form-control',
            'style':'max-width: 300px',
            'placeholder':'Enter date of birth'
         }),


      }

      department = ModelChoiceField(queryset=Our_student.objects.all())

      parent = ModelChoiceField(queryset=Our_student.objects.all(),
       )
     

class UserForm(ModelForm):
   class Meta:
      
      model = Our_user
      fields = ['first_name','last_name','username','email','phone','password','confirm_password']
      widgets = {
         

         'first_name': TextInput(attrs={
            'class': 'form-control',
            'style':'width:300px',
            'placeholder':'Enter first name'
         }),

         'last_name': TextInput(attrs={
            'class':'form-control',
            'style':'max-width: 300px',
            'placeholder':'Enter last name'
         }),

         
         'username': TextInput(attrs={
            'class':'form-control',
            'style':'max-width: 300px',
            'placeholder':'Enter username'
         }),

         'email': EmailInput(attrs={

            'class':'form-control',
            'style':'max-width: 300px',
            'placeholder':'Enter email'

         }),
         
          'phone': NumberInput(attrs={
             'class':'form-control',
             'style':'max-width:300px',
             'placeholder':'Enter phone number'
          }),

          'password': PasswordInput(attrs={
            'class':'form-control',
            'style':'max-width: 300px',
            'placeholder':'Enter password'
         }),

           'confirm_password': PasswordInput(attrs={
            'class':'form-control',
            'style':'max-width: 300px',
            'placeholder':'Confirm password'
         })
      }

class LoginForm(ModelForm):

   class Meta:

      model = Our_user
      fields = ['username','password']
      widgets = {

         'username': TextInput(attrs={

            'class':'form-control',
            'style':'max-width:300px',
            'placeholder':'Enter username'

         }),

         'password': PasswordInput(attrs={

            'class':'form-control',
            'style':'max-width:300px',
            'placeholder':'Enter password'
         })
      }