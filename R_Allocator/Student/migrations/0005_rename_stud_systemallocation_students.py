# Generated by Django 4.2.7 on 2023-11-26 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0004_remove_systemallocation_students_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='systemallocation',
            old_name='stud',
            new_name='students',
        ),
    ]
