from django.urls import path
from . import views


urlpatterns =[
    path('',views.index, name='index'),
    path('create_user/', views.create_user, name='create_user'),
    path('all_student/', views.all_students, name='all_student'),
    path('<int:id>', views.view_student, name='view_student'),
    path('delete/<int:id>', views.delete_student, name='delete_student'),
    path('add_student/', views.add_student, name='add_student' ),
    path('update_student/<int:id>', views.update_student, name='update_student'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout')
]