# Generated by Django 4.2.4 on 2023-09-25 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0015_testimonials_delete_student_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='email',
        ),
        migrations.RemoveField(
            model_name='student',
            name='field_of_study',
        ),
        migrations.RemoveField(
            model_name='student',
            name='gpa',
        ),
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.AddField(
            model_name='student',
            name='department',
            field=models.CharField(choices=[(' ', 'Select'), ('Science', 'Science'), ('Commercial', 'Commercial'), ('Art', 'Art')], default='Science', max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_number',
            field=models.UUIDField(default='122267', editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
