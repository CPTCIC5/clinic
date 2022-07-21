from django.shortcuts import render,get_object_or_404
from .models import Blog, Contact,Appointment,BlogComment
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from ratelimit.decorators import ratelimit



def index(request):
    return render(request,'home/index.html')

def about(request):
    return render(request,'home/about.html')


@ratelimit(key='ip',rate='10/d',block=True)
def contact(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone_no=request.POST.get('phone_no')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        if len(name) >50:
            messages.error(request,'Name Too Big')
            return HttpResponseRedirect(reverse('index:contact'))
        elif len(phone_no) >15:
            messages.error(request,'Phone no. Too Big')
            return HttpResponseRedirect(reverse('index:contact'))
        elif len(subject) > 50:
            messages.error(request,'Subject Too Big')
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


def blog(request):
    post=Blog.objects.all()
    return render(request,'home/blog.html',{'post':post})


@ratelimit(key='ip',rate='10/d',block=True)
def paginated_blog(request,title):
    queryset=get_object_or_404(Blog,title=title)
    if request.method == 'POST':
        commented_by=request.user
        message=request.POST.get('message')
        if len(message) > 150:
            messages.success(request,'Comment too big!')
            return HttpResponseRedirect(reverse('index:paginated-blog',args=[queryset.title]))
        else:
            entry=BlogComment(blog=queryset,commented_by=commented_by,message=message)
            entry.save()
            messages.success(request,'Comment Added Successfully!')
            return HttpResponseRedirect(reverse('index:paginated-blog',args=[title]))
    return render(request,'home/paginated_blog.html',{'queryset':queryset})


@ratelimit(key='ip',rate='5/d')
def appointment(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        print(name,email,phone)
        appointment_at = request.POST.get('appointment_at')
        problem = request.POST.get('problem')
        if len(name)>50:
            messages.error('name too big')
            return HttpResponseRedirect(reverse('index:appointment'))
        elif len(phone)>15:
            messages.error('Phone no. too big')
            return HttpResponseRedirect(reverse('index:appointment'))
        else:
            data=Appointment(name=name,email=email,phone=phone,appointment_at=appointment_at,problem=problem)
            data.save()
            data={
            'name':name,
            'email':email,
            'phone':phone,
            'appointment_at':appointment_at,
            'problem':problem
            }
            message='''
            New message : {}
            from : {}
            '''.format(data['problem'],data['phone'])
            send_mail(data['appointment_at'],data['phone'],message, '',['aryanjainak@gmail.com'] )
            messages.success(request,'Appointment Ticket Booked!')
            return HttpResponseRedirect(reverse('index:index'))
    return render(request,'home/appointment.html')