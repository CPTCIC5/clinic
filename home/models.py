from django.db import models

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