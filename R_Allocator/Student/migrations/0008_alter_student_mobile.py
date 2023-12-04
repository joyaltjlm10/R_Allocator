# Generated by Django 4.2.7 on 2023-11-28 07:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0007_alter_systemallocation_students_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Mobile',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: 'xxxxxxxxxx'. Up to 10 digits allowed.Don't Use Characters like !,@,#,$,%,^,&,*,etc", regex='^\\+?1?\\d{9,10}$')]),
        ),
    ]