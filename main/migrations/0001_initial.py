# Generated by Django 3.0.4 on 2020-03-06 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_full_name', models.CharField(max_length=200, verbose_name='Full Name')),
                ('user_description', models.CharField(blank=True, max_length=500, null=True)),
                ('user_experience', models.TextField(default='No experience:)', verbose_name='My Experience as a Django Developer')),
                ('user_knowledge', models.TextField(verbose_name='What I Know')),
                ('user_skill', models.TextField(verbose_name='Education and Training')),
                ('user_achievement', models.TextField(blank=True, null=True, verbose_name='My Achievements')),
            ],
        ),
    ]
