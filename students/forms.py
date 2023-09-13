from django import forms
from . models import *
from django.forms import *
from django.contrib.auth.models import User

class StudentForm(ModelForm):


   class Meta:
      
      model = Student
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

         'email': EmailInput(attrs={

            'class':'form-control',
            'style':'max-width: 300px',
            'placeholder':'Enter email'

         }),

          'field_of_study': TextInput(attrs={
            'class':'form-control',
            'style':'max-width: 300px',
            'placeholder':'Enter field of study'
         }),

           'gpa': NumberInput(attrs={
            'class':'form-control',
            'style':'max-width: 300px',
            'placeholder':'Enter GPA'
         }),


   
         'username': TextInput(attrs={

            'class':'form-control',
            'style': 'max-width:300px',
            'placeholder':'Select parent'
         })
      }

      parent = ModelChoiceField(queryset=Student.objects.all(),
       )
      parent.widget.attrs={
         'class':'form-control'
      }
     

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