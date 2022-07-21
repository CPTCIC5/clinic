from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone_no=models.CharField(max_length=15)
    subject=models.CharField(max_length=50)
    message=models.TextField()
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.time.year}-{self.time.month}-{self.time.day}"

    class Meta:
        ordering=['-time']

class Blog(models.Model):
    title=models.CharField(max_length=50,unique=True)
    image=models.ImageField(default='default-blog.jpeg',upload_to='blog-images')
    content=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    posted_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):  
        return self.title
    
    class Meta:
        ordering=['posted_on']

class Appointment(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    appointment_at=models.DateTimeField()
    problem=models.TextField()
    taken_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering=['-taken_on']

class BlogComment(models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
    comment_date=models.DateTimeField(auto_now_add=True)
    commented_by=models.ForeignKey(User,on_delete=models.CASCADE)
    message=models.CharField(max_length=150)

    def __str__(self):
        return f"{self.blog} - {self.commented_by}"

    class Meta:
        ordering=['comment_date']