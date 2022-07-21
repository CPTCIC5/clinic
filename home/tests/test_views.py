from urllib import response
from django.test import TestCase,Client
from django.urls import reverse
from home.models import Blog,Contact

class TestViews(TestCase):
    def setup(self):
        self.client = Client()

    def test_index_GET(self):
        response = self.client.get(reverse('index:index'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'home/index.html')

    def test_contact_POST(self):
        response = self.client.post(reverse('index:contact'),{
            'name':'automated-test',
            'email':'aryanjainak@gmail.com',
            'phone_no': '3434',
            'subject' : 'Subject',
            'message' : 'message hai'
        })
        self.assertEqual(response.status_code,302)
        query= Contact.objects.get(id=1)
        self.assertEqual(query.name,'automated-test')
