# Generated by Django 5.0.2 on 2024-02-29 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AIapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageai',
            name='image_ai',
            field=models.ImageField(blank=True, null=True, upload_to='mediaai'),
        ),
    ]
