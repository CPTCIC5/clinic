# Generated by Django 4.0.5 on 2022-07-15 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(default='default-blog.jpeg', upload_to='blog-images')),
                ('content', models.TextField()),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['posted_on'],
            },
        ),
    ]