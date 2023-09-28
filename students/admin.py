from django.contrib import admin
from . models import *

# Register your models here.

class StudentAdmin(admin.ModelAdmin):

    list_display=('first_name','last_name','parent')

class Our_userAdmin(admin.ModelAdmin):
    list_display = ('user', 'email')

admin.site.register(Our_student,StudentAdmin )
admin.site.register(Our_user, Our_userAdmin)
admin.site.register(Testimonials)
admin.site.register(Blog)
