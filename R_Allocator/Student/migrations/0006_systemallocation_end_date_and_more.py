# Generated by Django 4.2.6 on 2023-11-26 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0005_rename_stud_systemallocation_students'),
    ]

    operations = [
        migrations.AddField(
            model_name='systemallocation',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='systemallocation',
            name='start_date',
            field=models.DateField(null=True),
        ),
    ]
