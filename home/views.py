from django.shortcuts import render,get_object_or_404
from .models import *
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout as auth_logout
from django.core.mail import send_mail
from ratelimit.decorators import ratelimit



def index(request):
    return render(request,'home/index.html')

def about(request):
    return render(request,'home/about.html')


@ratelimit(key='ip',rate='10/d')
def contact(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone_no=request.POST.get('phone_no')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        if len(name) >50:
            messages.success(request,'Name Too Big')
            return HttpResponseRedirect(reverse('index:contact'))
        elif len(phone_no) >15:
            messages.success(request,'Phone no. Too Big')
            return HttpResponseRedirect(reverse('index:contact'))
        elif len(subject) > 50:
            messages.success(request,'Subject Too Big')
            return HttpResponseRedirect(reverse('index:contact'))
        else:
            contact_entry=Contact(name=name,email=email,phone_no=phone_no,subject=subject,message=message)
            contact_entry.save()
            data={
            'name':name,
            'email':email,
            'subject':subject,
            'phone_no':phone_no,
            'message':message
            }
            message='''
            New message : {}
            from : {}
            '''.format(data['message'],data['email'])
            send_mail(data['subject'],data['phone_no'],message, '',['aryanjainak@gmail.com'] )
            messages.success(request,'THANKS FOR CONTACTING US! WE WILL REACH TO U ASAP')
            return HttpResponseRedirect(reverse('index:index'))
    return render(request,'home/contact.html')

def logout(request):
    auth_logout(request)
    messages.success(request,'Logout Successful')
    return HttpResponseRedirect(reverse('home:index'))

def blog(request):
    post=Blog.objects.all()
    return render(request,'home/blog.html',{'post':post})

def paginated_blog(request,title):
    queryset=get_object_or_404(Blog,title=title)
    return render(request,'home/paginated_blog.html',{'queryset':queryset})