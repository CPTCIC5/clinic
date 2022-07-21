from django.test import TestCase
from home.models import Blog
from django.contrib.auth.models import User


class IndexModelTest(TestCase):
    def setUp(self):
        self.user=User.objects.create(
            username='admin',
            password='123'

        )
        self.x1=Blog.objects.create(
            title='x1',
            image='default-blog.jpeg',
            content='no content',
            author=self.user,
        )


    def test_blog_is_working(self):
        self.assertEqual(self.x1.title,'x1')