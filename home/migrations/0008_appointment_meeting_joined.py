# Generated by Django 4.0.5 on 2022-07-23 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_blog_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='meeting_joined',
            field=models.BooleanField(default=False),
        ),
    ]
