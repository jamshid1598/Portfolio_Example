# Generated by Django 3.0.4 on 2020-03-09 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_resume_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='user_image',
            field=models.ImageField(default='main/images/user_image.jpg', upload_to=''),
        ),
    ]