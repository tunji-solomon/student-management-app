from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *
from django.urls import reverse
from django.contrib import messages
from .forms import *
from django.contrib.auth import login,logout,authenticate
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def index(request):
    return render(request,'students/index.html')

# create user section
def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        confirm_password = request.POST.get('confirm_password')
        global context
        context ={'form':form}
        if password == confirm_password:
           if Our_user.objects.filter(username=username).exists():
               messages.info(request,'username already exist')
               return render(request,'students/create_user.html', context)
           else:
               if Our_user.objects.filter(email=email).exists():
                   messages.info(request,'email already exist')
                   return render(request,'students/create_user.html', context)
               else:
                   user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,
                               email=email,password=password)
                   user.save()
                   our_user = Our_user(user=user,username=username,first_name=first_name,last_name=last_name,
                               email=email,password=password,phone=phone)
                   our_user.save()
                   login(request,user)
                   subject = 'Student Management'
                   message = f'hello,Mr/Mrs {user.first_name} {user.last_name} \n Thank you for registering'
                   sender = settings.EMAIL_HOST_USER
                   receiver = [user.email]
                  # send_mail(subject,message,sender,receiver)
                   messages.info(request,'read code succesfully')
                   return HttpResponseRedirect(reverse('index'))
               

               
        else:
            messages.info(request,'Password and confirm password mismatch')
            return render(request,'students/create_user.html', context)
    else:
        form = UserForm()
    return render(request, 'students/create_user.html',{'form':form})

# user login section

def login_user(request):
        user_login = LoginForm()
        if request.method == 'POST':
           username= request.POST.get('username')
           password = request.POST.get('password')

           user = authenticate(username=username,password=password)
           if user is not None:
               login(request,user)
               subject = 'Account Login Notification'
               message = f'hello, {user.first_name} {user.last_name} \n \t Your account was logged into.\n If this is you, Kindly ignore this message, else contact us.\n Best regards.'
               sender = settings.EMAIL_HOST_USER
               receiver = [user.email]
               #send_mail(subject,message,sender,receiver)
               return HttpResponseRedirect(reverse('index'))
           else:
               print('unable to log in')
               user_login = LoginForm()
        return render(request,'students/login.html',{'form':user_login})

#  user logout section

def logout_user(request):
        logout(request)
        return HttpResponseRedirect(reverse('index'))

# display all student section

def all_students(request):
    context = {
        'students': Student.objects.all()
    }
    return render(request,'students/all_students.html',context)
        
# view student informationn section

def view_student(request,id):
    student = Student.objects.get(pk=id)
    return render(request,'students/details.html',{
        'students':student
        })

# add student section

def add_student(request):
    forms = StudentForm()
    if request.method == 'POST':
        new_student = StudentForm(request.POST)
        new_student.save()
        messages.info(request, 'Student added successfully')
        return HttpResponseRedirect(reverse('all_student'))
    return render(request, 'students/add_students.html',{'forms':forms})

# update student section

def update_student(request,id):
    if request.method == 'POST':
        students = Student.objects.get(pk=id)
        student_update = StudentForm(request.POST, instance=students)
        if student_update.is_valid():
            student_update.save()
            return HttpResponseRedirect(reverse('all_student'))

    else:
      students = Student.objects.get(pk=id)
      form = StudentForm(instance=students)

      return render(request,'students/update_student.html',{'form':form})
    
# delete student section
#     
def delete_student(request,id):
    student = Student.objects.get(pk=id)
    success = student.delete()
    if success:
        messages.info(request, 'Student record deleted successfully')
    else:
        messages.info(request,'Unable to delete student records')
    return HttpResponseRedirect(reverse('all_student'))




    