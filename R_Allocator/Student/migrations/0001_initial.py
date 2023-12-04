# Generated by Django 4.2.7 on 2023-11-24 09:49

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ResourceAllocator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('isactive', models.BooleanField(default=True, verbose_name='active')),
                ('Name', models.CharField(max_length=50)),
                ('Mobile', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: 'xxxxxxxxxx'. Up to 10 digits allowed.", regex='^\\+?1?\\d{9,10}$')])),
                ('Email', models.CharField(max_length=50)),
                ('Have_Own_System', models.BooleanField(default=False)),
                ('Batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ResourceAllocator.batch')),
                ('created_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Students',
            },
        ),
        migrations.CreateModel(
            name='SystemAllocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('students', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Student.student')),
                ('system', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ResourceAllocator.system')),
            ],
        ),
    ]