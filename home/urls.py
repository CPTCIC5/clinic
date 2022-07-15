from django.urls import path
from . import views

app_name='index'

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('blog/',views.blog,name='blog'),
    path('blog/<str:title>',views.paginated_blog,name='paginated-blog')
]