# Generated by Django 4.1.2 on 2022-10-06 06:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_profile_updated_alter_profile_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.IntegerField(max_length=225),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
