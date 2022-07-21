from django.contrib import admin
from .models import BlogComment, Contact,Blog,Appointment

admin.site.register(Contact)
admin.site.register(Blog)
admin.site.register(Appointment)
admin.site.register(BlogComment)